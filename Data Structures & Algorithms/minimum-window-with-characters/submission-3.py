class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        window = Counter()

        required = len(need)
        formed = 0
        min_len = float('inf')

        l = 0
        start = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1

            if ch in need and need[ch] == window[ch]:
                formed += 1
            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l
                    
                left_ch = s[l]
                window[left_ch] -= 1
                l += 1

                if left_ch in need and need[left_ch] > window[left_ch]:
                    formed -= 1
      
        if min_len == float('inf'):
            return ""
        return s[start: start+min_len]

