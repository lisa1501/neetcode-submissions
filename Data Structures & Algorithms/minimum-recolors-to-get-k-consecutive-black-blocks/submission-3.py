class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        count = 0

        l = 0
        for r in range(len(blocks)):
            if blocks[r] == "W":
                count += 1

            if r - l + 1 > k:
                if blocks[l] == "W":
                    count -=1
                l += 1

            if r - l + 1 == k:
                ans = min(ans, count)
        
        return ans