class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        i = 0 
        j = len(people)-1
        while i<=j:
            res = limit - people[j]
            boat+=1
            j-=1
            if i<=j and res>=people[i]:
                i+=1
        
        return boat



        