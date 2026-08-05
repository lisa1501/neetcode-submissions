class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        indexed_tasks = [
            (arrival, processing, index)
            for index, (arrival, processing) in enumerate(tasks)
        ]

        # Sort by arrival time.
        indexed_tasks.sort()

        heap = []
        answer = []
        
        i = 0                     
        time = 0                  
        n = len(tasks)

        while i < n or heap:
            # If no task is available,
            # jump directly to the next arrival time.
            if not heap:
                time = max(time, indexed_tasks[i][0])
            # Push every task that has already arrived
            while i < n and indexed_tasks[i][0] <= time:
                arrival, processing, index = indexed_tasks[i]
                heapq.heappush(
                    heap,
                    (processing, index)
                )
                i += 1
  
            # Choose the task with:
            # smallest processing time and smallest index
            processing, index = heapq.heappop(heap)
            answer.append(index)
            # CPU spends processing_time units finishing the task.
            time += processing

        return answer
        