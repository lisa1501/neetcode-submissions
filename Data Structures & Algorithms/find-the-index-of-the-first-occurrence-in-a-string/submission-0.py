class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time:  O(n * m) Space: O(1)
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):

            # Check whether needle starts at i
            match = True

            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break

            if match:
                return i

        return -1
        