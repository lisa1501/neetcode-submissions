class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(l, r) :
            while l < r:
                while l < r and not s[l].isalnum():
                    l += 1

                while r > l and not s[r].isalnum():
                    r -= 1

                if s[l].lower() != s[r].lower():
                    return False
                l+=1
                r-=1
            return True

        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return isPalindrome(l+1, r) or isPalindrome(l, r-1)

            l+=1
            r-=1
        return True
        