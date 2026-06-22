class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []

        # used[i] tells us whether nums[i]
        # is already placed into the current permutation
        used = [False] * n

        def dfs():

            if len(path) == n:
                res.append(path[:])
                return

            # =====================================
            # TRY EVERY UNUSED NUMBER
            # =====================================

            for i in range(n):

                # If this number is already used
                # in the current permutation,
                # skip it.
                if used[i]:
                    continue

                # =================================
                # CHOOSE nums[i]
                # =================================

                # Mark it as used
                used[i] = True

                # Add number to current permutation
                path.append(nums[i])

                # Explore all permutations
                # that start with the current path.
                dfs()

                # =================================
                # BACKTRACK
                # =================================

                # Remove the number we just added.
                path.pop()

                # Mark it unused again.
                #
                # This allows future branches
                # to use this number.
                used[i] = False

        dfs()

        return res
        