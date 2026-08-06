class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort (Kahn's Algorithm)
        # Build a graph and compute number of prerequisites for each course in list. idx is the coure, ele of idx how many pre course needed for startthe course
        # Add all courses with indegree = 0 into a queue.
        # while q is not empty, remove a precourse from queue, finished +=1
        # reduce the next course(in the list) of poped precourse , if next course where in the list , == 0, append it to queue
        # check if finished equal to given num of course
        # Time: O(V+E) Space: O(V+E), V is num of course, E is num of prerequisites
        pre_to_courses = defaultdict(list)
        req_cnt_course = [0] * numCourses
        for course, pre_course in prerequisites:
            pre_to_courses[pre_course].append(course)
            req_cnt_course[course] += 1
        
        q = deque()
        for course in range(numCourses):
            if req_cnt_course[course] == 0:
                q.append(course)
        
        completed = 0
        while q:
            pre_course = q.popleft()
            completed += 1

            for next_course in pre_to_courses[pre_course]:
                req_cnt_course[next_course] -= 1

                if req_cnt_course[next_course] == 0:
                    q.append(next_course)

        return completed == numCourses






