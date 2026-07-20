class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Number of elements
        n = len(nums)

        # Final answer:
        # Sum of XOR values of every subset
        total = 0

        def dfs(i, current_xor):
            nonlocal total

            # -------------------------
            # Base case
            # -------------------------
            # We have made a Pick/Skip decision for every number.
            #
            # current_xor is now the XOR
            # of the current subset.
            if i == n:
                total += current_xor
                return

            # -------------------------
            # Choice 1: Pick nums[i]
            # -------------------------
            # Include nums[i] in the subset.
            # Update the running XOR.
            dfs(i + 1, current_xor ^ nums[i])

            # -------------------------
            # Choice 2: Skip nums[i]
            # -------------------------
            # Leave the XOR unchanged.
            dfs(i + 1, current_xor)

        # Start with: index = 0, XOR = 0 (empty subset)
        dfs(0, 0)

        return total