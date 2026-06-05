class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs))==1:
            return strs[0]
        sonted_strs=sorted(strs)
        print(sonted_strs)
        l = min(len(sonted_strs[0]), len(sonted_strs[1]))
        print(l)
        for i in range(l):
            if sonted_strs[0][i] != sonted_strs[-1][i]:
                return sonted_strs[0][:i]
        return sonted_strs[0]
        
        