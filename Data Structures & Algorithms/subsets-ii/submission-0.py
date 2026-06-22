class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        # Stores all subsets
        res = []

        # Current subset being built
        path = []

        n = len(nums)

        def dfs(i):

            # Base case:
            # We have decided for every number whether
            # to pick it or skip it.
            if i == n:

                # Save a copy of the current subset
                res.append(path[:])

                return

            # ==================================
            # CHOICE 1: PICK nums[i]
            # ==================================

            # Add current number into subset
            path.append(nums[i])

            # Continue making decisions
            # for the remaining numbers
            dfs(i + 1)
            # Backtrack:
            # Undo the pick so we can explore
            # the "skip" branch next
            path.pop()

            # skip all duplicates
            j = i
            while j + 1 < n and nums[j] == nums[j + 1]:
                j += 1

            dfs(j + 1)

        dfs(0)

        return res