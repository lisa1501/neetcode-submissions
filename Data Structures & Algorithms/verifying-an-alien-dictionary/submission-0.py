class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            w1 = [rank[c] for c in words[i]]
            w2 = [rank[c] for c in words[i+1]]
            print(i,w1)
            print(i,w2)

            if w1 > w2:
                return False

        return True
