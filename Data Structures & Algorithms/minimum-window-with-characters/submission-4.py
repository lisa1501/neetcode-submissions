class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        res_len = float('inf')
        have = 0
        re_start = 0

        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1

            if ch in need and need[ch] == window[ch]:
                have += 1

            while have == len(need):
                if r - l + 1 < res_len:
                    res_len = r-l+1
                    re_start = l

                left_ch = s[l]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                l += 1

        if res_len == float('inf'):
            return ""
        return s[re_start:re_start+res_len]
