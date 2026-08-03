class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # frequency of chars
        # init res
        # loop through words,init frequency for word, init a bool good is true, 
        # loop through word in words, update frequency
        # if letter fruency in word greater than frequency of chars , good is false, break
        # else good is True, increase res by len(word)
        
        # Time O(n + m*k) => n len(chars), m len(words) k len(longest word)
        # Space: O(1) 26 different Engh letters
        count = Counter(chars)
        res = 0

        for word in words:
            cur_word = defaultdict(int)
            good = True
            for ch in word:
                cur_word[ch] += 1
                if cur_word[ch] > count[ch]:
                    good = False
                    break
            if good:
                res += len(word)

        return res