class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time: O(n) n is len(s)
        # space: O(m) m is unique letters in s
        seen = set()
        res = 0
        l = 0
        for r in range(len(s)):
            # s="pwwkew" 
            # if s[r] in seen: this is not working
            # r=0,l=0,seen={p},res=1
            # r=1,l=0,seen={p,w},res=2
            # r=2,l=0,seen={w},l=1,seen={w,w}=>{w}, res=2
            # r=3,l=1,seen={w,k},res=3
            # r=4,l=1,seen={w,k,e},res=4
            # r=5,l=1,seen={k,e},l=2,seen={k,e,w}, res=4
            while s[r] in seen:
            # r=0,l=0,seen={p},res=1
            # r=1,l=0,seen={p,w},res=2
            # r=2,l=0,seen={p,w},remove s[l]from seen, seen={w} l=1
                # s[r] is w, still in seen, remove it from seen,seen={} l=2 
                # add s[r] to seen, {w}, res= (2-2+1)=1
            # r=3,l=2,seen={w,k},res=2
            # r=4,l=2,seen={w,k,e},res=3
            # r=5,l=2,seen={w,k,e},remove s[l]from seen, seen={k,e} l=3
                # seen={k,e,w} res=(5-3+1)
                seen.remove(s[l])
                l += 1
            seen.add(s[r]) 
            res = max(res, r - l +1)

        return res

        
        