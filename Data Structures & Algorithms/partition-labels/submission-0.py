class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # time:O(n) space:O(1)
        ch_to_idx = {}
        for i,ch in enumerate(s):
            ch_to_idx[ch] = i

        result = []
        start = 0
        end = 0

        for i,ch in enumerate(s):
            # This character must be contained through its last occurrence.
            end = max(end, ch_to_idx[ch])
            # All characters in this partition have now finished.
            if i == end:
                result.append(end - start + 1)
                start = i + 1
                
        return result
        