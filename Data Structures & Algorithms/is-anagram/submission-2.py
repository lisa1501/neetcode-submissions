class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        ord_s = [0]*26
    
        for i in range(len(s)):
            ord_s[ord(s[i]) - ord('a')] +=1
            ord_s[ord(t[i]) - ord('a')] -=1

        for ele in ord_s:
            if ele != 0:
                return False
        return True
        



        