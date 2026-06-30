class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()

        i = 0
        j = len(people) - 1
        while i <= j:
            res = limit - people[j]
            
            boats += 1
            j -= 1

            if res >= people[i]:
                i += 1
        return boats
