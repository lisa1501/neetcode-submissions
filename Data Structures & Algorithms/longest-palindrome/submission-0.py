class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0
        for ch in s:
            count[ch] += 1
            if count[ch] %2 == 0:
                res += 2

        return res + (res < len(s))
        