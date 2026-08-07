class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # map order, key is letter, value is very last idx
        # loop through words, adjacent pairs w1,w2
        # if len(w1) > len(w2) => false
        # w1&w2 same idx are differen letter, 
        # check these two letters idx val in map, 
        # if w1 letter idx val > w1 letter idx val => false
        # If all adjacent pairs pass validation, return true
        # Time: O(n*m) n:len(words), m:len(word), Space:O(1)
        order_idx = {}
        for i, ch in enumerate(order):
            order_idx[ch] = i

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False

                if w1[j] != w2[j]:
                    if order_idx[w1[j]] > order_idx[w2[j]]:
                        return False
                    break

        return True