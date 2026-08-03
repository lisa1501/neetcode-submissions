class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        print(freq)
        max_val = float("-inf")
        for key in freq:
            if freq[key] == key:
                max_val = max(max_val, key)
        if max_val == float("-inf"):
            return -1
        return max_val