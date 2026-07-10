class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        l = 0
        r = 0
        while r <len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                ans = max(ans, r - l + 1)
                r+=1

        return ans

        
        