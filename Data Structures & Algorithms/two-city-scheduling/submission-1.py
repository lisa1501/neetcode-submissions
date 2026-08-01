class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Send exactly half people to city A and half to city B.
        # Each person: [A cost, B cost]
        # Calculate: difference = A - B
        # Sort. People who benefit most from A go first.
        # Time: O(nlogg) Space:O(1)
        # costs=[[10,20],[30,200],[400,50],[30,20]]
        costs.sort( key=lambda x:x[0]-x[1])
        print(costs)
        # [[30, 200], [10, 20], [30, 20], [400, 50]]
        n = len(costs)//2

        ans = 0

        for i in range(len(costs)):

            if i < n:
                ans += costs[i][0]
            else:
                ans += costs[i][1]

        return ans
        

        