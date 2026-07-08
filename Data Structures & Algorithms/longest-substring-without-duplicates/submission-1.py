class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        l = 0 
#  s="pwwkew" 
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l]) 
                l += 1 
            seen.add(s[r])  
# seen = (pw)=>(w),l=1=>(),l=2 (w)=>(wke) l=2=>(ke) l =3 (kew)
            ans = max(ans, r-l+1)
        return ans
        