class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        # uppercase and lower case
        #  s = "race car", t = "carrace"-> wihout space
        #  numbers, sympbols -> letters
        #  s ="" t ="" -> not an empty string
        

        #  hashmap, key -> letter, values frequency 
        #  compare two hashmap s and t
        #  time: O(on) space: O(1)

        # count_s = {}
        # count_t = {}
        # for char in s:
        #     if char not in count_s:
        #         count_s[char] =1
        #     else:
        #         count_s[char] = +1
        # for char in t:
        #     if char not in count_t:
        #         count_t[char] =1
        #     else:
        #         count_t[char] = +1

        # return count_s==count_t

# solution 2

        if len(s) != len(t):
            return False
        count = [0]*26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] +=1
            count[ord(t[i]) - ord('a')] -=1

        for num in count:
            if num !=0:
                return False
        return True

        



        







        