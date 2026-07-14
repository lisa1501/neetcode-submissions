class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)

        ans = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                ans += 1
            else:
                prevEnd = intervals[i][1]
        return ans
        