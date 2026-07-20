class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        path = []
        def dfs(i):
            if i == n:
                res.append(path[:])
                return 
            # choose nums[i]
            path.append(nums[i])
            # after choosing nums[i], explore next
            dfs(i+1)
            # Undo
            path.pop()

            #skip nums[i]
            dfs(i+1)
        dfs(0)
        return res