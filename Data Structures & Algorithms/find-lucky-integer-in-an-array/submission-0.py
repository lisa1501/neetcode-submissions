class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        print(freq)
        max_val = -1
        for key in freq:
            if freq[key] == key:
                max_val = max(max_val, key)
        return max_val