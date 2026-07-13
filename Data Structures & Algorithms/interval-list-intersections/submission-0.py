class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        first = second = 0
        while first < len(firstList) and second < len(secondList):
            first_start, first_end = firstList[first]
            second_start, second_end = secondList[second]

            start = max(first_start, second_start)
            end = min(first_end, second_end)

            if start <= end:
                res.append([start, end])

            if first_end < second_end:
                first += 1
            else:
                second += 1
                
        return res
        