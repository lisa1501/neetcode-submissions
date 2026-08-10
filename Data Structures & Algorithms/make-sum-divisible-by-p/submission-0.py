class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # time:O(n) space:O(n)
        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0

        last_seen = {0: -1}
        prefix = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            needed = (prefix - remainder) % p

            if needed in last_seen:
                length = i - last_seen[needed]
                min_len = min(min_len, length)

            last_seen[prefix] = i

        if min_len == len(nums):
            return -1

        return min_len