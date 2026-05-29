class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ord_s = [0]*26
        ord_t = [0]*26
        for chr in s:
            ord_s[ord(chr) - ord('a')] +=1


        for chr in t:
            ord_t[ord(chr) - ord('a')] +=1
        return ord_s==ord_t
        



        