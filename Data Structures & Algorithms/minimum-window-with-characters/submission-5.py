class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # time:O(n+m) n:len(s), t:len(t), space:O(k) k: unique letters in s, t
        need = Counter(t)
        window = defaultdict(int)
        res_len = float('inf')
        res_start = 0
        have = 0

        l = 0
        for r in range(len(s)):
            # add right character
            ch = s[r]
            window[ch] += 1
            # character requirement satisfied
            if ch in need and window[ch] == need[ch]:
                have += 1
            # shrink while valid
            while have == len(need):
                # update answer
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_start = l
                # remove left character
                left_ch = s[l]
                window[left_ch] -= 1
                # window is no longer valid
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                l += 1
        if res_len == float('inf'):
            return ""
        return s[res_start: res_start + res_len]

        