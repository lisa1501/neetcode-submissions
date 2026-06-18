class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        # Example:
        # tasks = ["A","A","A","B","B","B"]
        # freq = {'A': 3, 'B': 3}
        freq = Counter(tasks)

        # Python only has a min heap.
        # Store negative counts to simulate a max heap.
        #
        # Example:
        # heap = [-3, -3]
        #
        # The task with highest remaining frequency
        # will always be popped first.
        heap = [-c for c in freq.values()]
        heapq.heapify(heap)

        # Stores tasks currently in cooldown.
        #
        # Each element:
        # (time_when_available_again, remaining_count)
        #
        # Example:
        # [(4, -2)]
        #
        # Means:
        # This task can be scheduled again at time = 4
        cooldown = deque()

        # Current simulated time
        time = 0

        # Continue until:
        # 1. No runnable tasks in heap
        # 2. No tasks waiting in cooldown
        while heap or cooldown:

            # Every iteration represents 1 CPU interval
            time += 1

            # If there is at least one available task,
            # execute the most frequent one.
            if heap:

                # Pop highest frequency task
                #
                # Example:
                # -3 -> -2
                #
                # Meaning:
                # We used one occurrence of that task
                cnt = heapq.heappop(heap) + 1

                # If task still has remaining executions,
                # put it into cooldown.
                #
                # Example:
                # time = 1
                # n = 2
                #
                # Task executed now cannot run again
                # until time = 3
                if cnt:
                    cooldown.append((time + n, cnt))

            # Check whether the front task has finished cooling down.
            #
            # Because cooldown queue is ordered by time,
            # only need to inspect the front.
            if cooldown and cooldown[0][0] == time:

                # Task becomes available again
                _, cnt = cooldown.popleft()

                # Put it back into heap so it can compete
                # with other available tasks
                heapq.heappush(heap, cnt)

        # Total intervals needed
        return time