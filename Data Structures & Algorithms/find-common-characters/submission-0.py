class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # count of words[0]
        # loop through words, count of word
        # update count of words[0] by min frequency of ch in count and word ocunt
        # initial empty list
        # loop through count of words[0], 
        #  list append key how many times = count of words[0] [key]
        # return res
        # time: O(n*m) space:O(1)
        count = Counter(words[0])

        for word in words:
            word_count = Counter(word)

            for c in count:
                count[c] = min(count[c], word_count[c])

        res = []
        for c in count:
            for i in range(count[c]):
                res.append(c)
        return res