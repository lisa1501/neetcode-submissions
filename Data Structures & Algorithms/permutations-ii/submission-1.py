class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        used = [False] * n

        def dfs(path):

            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):

                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True

                path.append(nums[i])

                dfs(path)

                path.pop()

                used[i] = False

        dfs([])

        return res