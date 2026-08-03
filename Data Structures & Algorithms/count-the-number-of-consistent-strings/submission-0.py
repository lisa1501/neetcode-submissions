class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # set of allowed
        # initialize ans with len(words)
        # loop through word , ch in word:
        # if ch not in allowed, decrease ans by 1, and break return ans
        # loop through done, return ans

        # time: O(n*l + m) m is len(allowed), n is len(words), l is len(longest word in words)
        # Space: O(m), m is len(allowed)

        allowed = set(allowed)

        res = len(words)
        for word in words:
            for ch in word:
                if ch not in allowed:
                    res -= 1
                    break

        return res
