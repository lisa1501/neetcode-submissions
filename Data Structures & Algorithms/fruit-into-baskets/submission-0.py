class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        ans = 0 
        l = 0
        for i in range(len(fruits)):
            freq[fruits[i]] +=1
            while len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l +=1
            ans = max(i-l+1, ans)

        return ans
        