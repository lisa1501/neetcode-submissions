class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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

                used[i] = True

                path.append(nums[i])

                dfs(path)

                path.pop()

                used[i] = False

        dfs([])

        return res
        