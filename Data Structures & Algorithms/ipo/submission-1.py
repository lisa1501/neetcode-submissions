class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Sort by required capital
        projects = sorted(zip(capital, profits))
        print(projects)
        # [(0, 1), (1, 2), (1, 3), (3, 4)]

        max_heap = []      # store profits (negative values)
        i = 0

        for _ in range(k):

            # Add all projects we can currently afford
            while i < len(projects) and projects[i][0] <= w:

                cap, profit = projects[i]
                heapq.heappush(max_heap, -profit)
                i += 1

            # No affordable projects
            if not max_heap:
                break

            # Pick the most profitable project
            w += -heapq.heappop(max_heap)

        return w