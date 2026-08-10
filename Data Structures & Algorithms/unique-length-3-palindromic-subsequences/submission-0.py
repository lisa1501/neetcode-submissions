class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # time:O(n) space:O(1)
        first_seen = {}
        last_seen = {}

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            if ch not in first_seen:
                first_seen[ch] = i

            last_seen[ch] = i

        res = 0

        # Try every character as the outer character
        for ch in first_seen:
            left = first_seen[ch]
            right = last_seen[ch]

            # Need at least one character between them
            if left < right:
                middle = set(s[left + 1:right])

                res += len(middle)

        return res