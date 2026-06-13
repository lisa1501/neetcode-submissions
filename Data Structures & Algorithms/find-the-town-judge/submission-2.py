class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = [0]*(n+1)
        outdeg = [0]*(n+1)

        for a,b in trust:
            indeg[a] +=1
            outdeg[b] +=1

        for i in range(len(indeg)):
            if indeg[i] == 0 and outdeg[i]==n-1:
                return i
        return -1

