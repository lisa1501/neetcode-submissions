class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # early return false if len of s and t are not same
        # s and t consist of lowercase English letters. create a list size of 26 , every index value is 0
        # loop through in range len s , 
        # increase list index by one, list idex ord(s[i]) - ord('a')
        # decrease list index by one, list idex ord(t[i]) - ord('a')
        # loop through created list, if there is element != 0 => false
        # return True
        # Time: O(n+m) => n is len s, m is len t
        # Space: O(1) = we have at most 26 different characters.
 
        if len(s) != len(t):
            return False

        arr = [0] * 26

        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1

        for num in arr:
            if num != 0:
                return False
        return True



        

        

        



        







        