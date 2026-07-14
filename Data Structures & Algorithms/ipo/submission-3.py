class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Input: k = 3, w = 0, 
        # profits = [1,4,2,3], 
        # capital = [0,3,1,1],
        # n projects , n len(profits),
        # one project = profits[i] and capital[i]
        # initial capital is W, 
        # for one project, 
        # for starting this project, we need capital[i] but if capital[i] <= w, we can start this project
        # after finishing this project we will get profits[i] 
        # in the end return total of max capital W
        # every time we need max profit, 

        # first sort profits ans capital, by capital, zip, 
        # loop through k
        # loop through sorted list 
        # if current project capital <=w:
        # use, store max profit. [-8.-7], by using negative profit.
        # if heap is empty, return 0
        # update W by the current project profits, notice change negative to pos
        # return w
        # time : O(nlogk) => n is len(capitals) k => givien k
        # space: O(n)

        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break
            
            w += -heapq.heappop(max_heap)

        return w



        



        
        