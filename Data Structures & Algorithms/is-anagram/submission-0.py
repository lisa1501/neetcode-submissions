class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.makehm(s) == self.makehm(t);

    def makehm(self, s: str) -> dict:
        hs = {};
        for char in s:
            if char not in hs:
                hs[char] = 1;
            else:
                hs[char] += 1;
        return hs;

        



        