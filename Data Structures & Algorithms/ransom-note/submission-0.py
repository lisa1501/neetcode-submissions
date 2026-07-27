class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp1 = {}
        mp2 = {}
        for ch in ransomNote:
            mp1[ch] = mp1.get(ch, 0) + 1

        for ch in magazine:
            mp2[ch] = mp2.get(ch, 0) + 1
        print(mp1)
        print(mp2)
        for ch in mp1:
            if ch not in mp2:
                return False
            if mp1[ch] > mp2[ch]:
                return False
        return True
        