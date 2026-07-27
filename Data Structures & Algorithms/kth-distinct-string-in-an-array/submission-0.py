class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mp = {}
        for ch in arr:
            mp[ch] = mp.get(ch, 0) + 1

        for ch in arr:
            if mp[ch] == 1:
                k -= 1
                if k == 0:
                    return ch
        return ""
        