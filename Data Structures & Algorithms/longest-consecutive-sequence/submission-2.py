class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        new_nums = set(nums)
        ans = 0
        longest = 0
        for num in new_nums:
            if num - 1 not in new_nums:
                longest = 1
                while num + 1 in new_nums:
                    num = num + 1
                    longest = longest + 1
            ans = max(ans, longest)
        return ans

        