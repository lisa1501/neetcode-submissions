# A graph is a valid tree if:
# It has no cycles
# It is fully connected
# If number of edges > n - 1, return false.
# Initialize DSU with n components.
# For each edge (u, v):
# If union(u, v) fails → cycle detected → return false.
# After processing all edges:
# Check if number of components is 1.
# Return true if only one component exists, else false
# Time:(V+(E*α(V))), space: O(V)
# V:number of vertices,E:number of edges in the graph. α() isused for amortized complexity.
class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        # every node is root of itself, 
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        # we are unioning child and parent, if child and parent has same parent, this is impossible, this means there is a cycle in grandparent, parent, child, so this is not tree,
        if pu == pv:
            return False

        self.comps -= 1
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return False

        return dsu.components() == 1

    

        