class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l_s = len(s)
        l_t = len(t)
        i = 0
        j = 0
        while i<l_s and j<l_t:
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == l_s 
        