class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1

        for i in range(len(s)):
            ch = s[i]
            
            if mp[ch] == 1:
                return i
        return -1
        