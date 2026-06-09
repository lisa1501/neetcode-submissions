class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [5] , 3 =>  0
        # [0,] => not an edge case
        # limit < 0 => not an edge case
        # time: O(nlogn) space :O(1)
        
        # 2 pointers, i left ,and j right ,  0 boat 
        i = 0
        j = len(people) -1
        boat = 0
        # sort the list [1,2,4,5]
                        # ^ ^

                        # [1,3,2,3,2] => [1,2,2,3,3]
                        #                   ^
                                        #   ^
        people.sort()
        # grab the number from very last, 5 , 6-5=1
        while i <= j:
            res = limit - people[j] # 0, 0,1
            j -= 1 # 3,2,1,
            # increase boat
            boat+=1 # 1, 2,3
        # check the res number is >= or no the number indx i
            if res>=people[i]:
                # if it is greater , i increase by 1
                i +=1#1
        return boat
       

        


 


        



        