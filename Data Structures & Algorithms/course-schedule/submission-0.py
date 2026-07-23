class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        # Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
        # graph = {1:[0], 0:[1]}
        # indegree = [1,1]

        # Input: numCourses = 2, prerequisites = [[0,1]]
        # graph = {1:[0]}
        # indegree = [1,0]
        queue = deque()

        # Courses without prerequisites
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        # queue = ([1])
        completed = 0

        while queue:

            course = queue.popleft() #course=1,#course=2
            completed += 1 #completed=1#completed=2

            for next_course in graph[course]: #0

                indegree[next_course] -= 1 #[0,0]

                if indegree[next_course] == 0:
                    queue.append(next_course) #queue = ([0])

        return completed == numCourses