class DSU:
    def __init__(self, n):
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

        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        