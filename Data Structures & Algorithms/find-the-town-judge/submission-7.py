class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_me = [0] * (n+1)
        trust_other = [0] * (n+1)
        
        for a, b in trust:
            trust_me[b] += 1
            trust_other[a] += 1

        for i in range(n+1):
            if trust_other[i] == 0 and trust_me[i] == n-1:
                return i

        return -1

        


        