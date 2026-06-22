class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = [] 
        path = [] 
        n = len(candidates) 

        def dfs(start, remain): 
            # found valid combination 
            if remain == 0: 
                res.append(path[:]) 
                return 
            # impossible 
            if remain < 0: 
                return 

            for i in range(start, n): 
                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # choose candidates[i] 
                path.append(candidates[i]) 
                # reuse allowed 
                dfs(i+1, remain - candidates[i]) 
                # backtrack 
                path.pop() 
        dfs(0, target) 
        return res