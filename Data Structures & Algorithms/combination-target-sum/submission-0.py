class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        path = [] 
        n = len(nums) 

        def dfs(start, remain): 
            # found valid combination 
            if remain == 0: 
                res.append(path[:]) 
                return 
            # impossible 
            if remain < 0: 
                return 

            for i in range(start, n): 
                # choose candidates[i] 
                path.append(nums[i]) 
                # reuse allowed 
                dfs(i, remain - nums[i]) 
                # backtrack 
                path.pop() 
        dfs(0, target) 
        return res
        