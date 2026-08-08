class Solution:
    def checkValidString(self, s: str) -> bool:
        # time:O(n) space:O(1)
        l_min = 0 #the minimum possible number of unmatched '('
        l_max = 0 #the maximum possible number of unmatched '('
        
        for ch in s:
            if ch == "(":
                l_min = l_min + 1
                l_max = l_max + 1
            elif ch == ")":
                l_min = l_min - 1
                l_max = l_max - 1
            else:
                l_min = l_min - 1
                l_max = l_max + 1

            if l_max < 0:
                return False
            if l_min < 0:
                l_min = 0

        return l_min == 0
            



        