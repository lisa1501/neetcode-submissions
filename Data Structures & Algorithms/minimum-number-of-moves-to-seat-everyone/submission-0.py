class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # sort seats, students => two O(n log n)
        # initialize moves is zero
        # loop througth of seats, students => O(n)
        # increase moves by abs(seat-, student)
        # return moves
        # Time: O(n log n) Space: O(1)
        seats.sort()
        students.sort()

        moves = 0

        for seat, student in zip(seats, students):
            moves += abs(seat - student)
            
        return moves
        