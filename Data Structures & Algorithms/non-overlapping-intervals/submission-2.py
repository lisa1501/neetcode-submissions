class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # time:O(nlogn) space: O(1) or O(n) depending on the sorting algo
        intervals.sort(key=lambda x: x[1])

        prev_end = intervals[0][1]
        ans = 0
        for i in range(1,len(intervals)):
            s,e = intervals[i]
            if s < prev_end:
                ans += 1
            else:
                prev_end = e
        return ans