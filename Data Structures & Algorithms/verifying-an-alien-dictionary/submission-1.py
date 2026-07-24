class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {}
        for i in range(len(order)):
            ch = order[i]
            order_index[ch] = i

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for j in range(len(w1)):

                if j == len(w2):
                    return False

                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
        return True


