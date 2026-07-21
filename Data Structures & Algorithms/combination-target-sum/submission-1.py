class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        n = len(nums) 

        def dfs(start, remain, path): 
            
            if remain == 0: 
                res.append(path[:]) 
                return 
                
            if remain < 0: 
                return 

            for i in range(start, n): 
                path.append(nums[i]) 
                dfs(i, remain - nums[i], path) 
                path.pop() 

        dfs(0, target, []) 
        return res
        