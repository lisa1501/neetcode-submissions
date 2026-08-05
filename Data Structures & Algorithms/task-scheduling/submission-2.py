class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # time: O(n)=> n len tasks, space: O(1) = 26letters
        # Count how many times each task appears
        freq = Counter(tasks) 
        # Max heap (Python only has min heap, so store negative counts)
        heap = [-c for c in freq.values()]
        heapq.heapify(heap)
        # Queue storing tasks in cooldown:
        # (time_when_available_again, remaining_count)
        cooldown = deque()
        time = 0
        # Continue until no ready tasks and no cooling tasks
        while heap or cooldown:
            # One CPU cycle passes
            time += 1 
            # Execute the highest-frequency available task
            if heap:
                count = heapq.heappop(heap) 
                # One occurrence has been used
                count += 1 
                # If more copies remain, put into cooldown
                if count < 0:
                    cooldown.append((time + n, count)) 
            # If the front task has finished cooling, move it back into the heap
            if cooldown and cooldown[0][0] == time: 
                _, count = cooldown.popleft() 
                heapq.heappush(heap, count) 

        return time



            
 

        
        