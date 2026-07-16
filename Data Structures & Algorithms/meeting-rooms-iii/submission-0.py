class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # [[1, 10], [2, 10], [3, 10], [4, 10]]
        available = [i for i in range(n)]  # Min heap for available rooms
        used = []  # Min heap for used rooms [(end_time, room_number)]
        count = [0] * n  # Count of meetings for each room

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            # [(10,0),(10,1)]
            count[room] += 1
            #[1,1]
        print(count)
        return count.index(max(count))
        