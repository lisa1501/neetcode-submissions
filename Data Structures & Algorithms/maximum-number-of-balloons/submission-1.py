class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # loop through text, 
        # if char in "balon", store frequency of char in a hashmap
        # if hashmap key smaller than 5, couldn't make "balon", return 0
        # "balloon" has 2 "l", 2 "o", reduce their frequncies by //2
        # return min frequency
        # time: O(n)=> n is len of text, Space: O(1)=> balloon has 5 different chars

        freq = defaultdict(int)
        target = set("balloon")
        l = len(target)
        for ch in text:
            if ch in target:
                freq[ch] += 1

        if len(freq) < l:
            return 0
        

        freq["l"] //= 2
        freq["o"] //= 2

        return min(freq.values())

        


        
        


        