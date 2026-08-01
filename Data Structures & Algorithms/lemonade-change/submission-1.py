class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # initialize five and ten is 0
        # loop through bills:
        # if 5, we don't need to provide change, increase five by 1
        # if 10, check do we have five or no, if we don't have, False, else increase ten by 1, decrease five by 1,
        # if 20, usually we give customer change is 
        # option1 one 10 and one 5 : 10+5 (prefer)
        # if ten > 0 and 5 > 0 , decrease them by 1
        # option2 three 5: 5+5+5
        # if five > 3 : decrease five by 3
        # if we couldn't make both of above two options return false
        # loop is done, return True
        # Time: O(n), Space: O(1)

        five = ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:     
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
                


        