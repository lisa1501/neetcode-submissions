class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        path = []

        def twoSum(start: int, target: int) -> None:
            """
            Find all pairs whose sum equals target.
            """

            left = start
            right = len(nums) - 1

            while left < right:

                current_sum = nums[left] + nums[right]

                if current_sum < target:
                    left += 1

                elif current_sum > target:
                    right -= 1

                else:
                    # Found one valid triplet.
                    result.append(path + [nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate values.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        def kSum(k: int, start: int, target: int) -> None:
            """
            Find all combinations of k numbers that sum to target.
            """

            # Base case: solve 2Sum with two pointers.
            if k == 2:
                twoSum(start, target)
                return

            # Choose one number, then recursively solve (k-1)-Sum.
            for i in range(start, len(nums) - k + 1):

                # Skip duplicates.
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Choose.
                path.append(nums[i])

                # Explore.
                kSum(k - 1, i + 1, target - nums[i])

                # Undo choice (backtrack).
                path.pop()

        kSum(3, 0, 0)

        return result
        
        