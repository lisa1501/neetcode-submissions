class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        n = len(nums)

        def dfs(i):
            if i == n:
                res.append(path[:])
                return
            #choose
            path.append(nums[i])
            #explore next
            dfs(i+1)
            #undo
            path.pop()
            # while duplicate, move pointer to next one
            j = i
            while j+1 < n and nums[j] == nums[j+1]:
                j+=1
            #skip
            dfs(j+1)

        dfs(0)
        return res