class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mpST = {}
        mpTS = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if((c1 in mpST and mpST[c1] != c2) or (c2 in mpTS and mpTS[c2] != c1)):
                return False

            mpST[c1] = c2
            mpTS[c2] = c1

        return True

        