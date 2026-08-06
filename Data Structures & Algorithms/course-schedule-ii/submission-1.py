class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort (Kahn's Algorithm)
        # Build a graph and compute number of prerequisites for each course in list. idx is the coure, ele of idx how many pre course needed for startthe course
        # Add all courses with indegree = 0 into a queue.
        # while q is not empty, remove a precourse from queue, add precourse into a list 
        # reduce the next course(in the list) of poped precourse , if next course where in the list , == 0, append it to queue
        # check if list len equal to given num of course, return list else return []
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
        
        order = []
        while q:
            pre_course = q.popleft()
            order.append(pre_course)

            for next_course in pre_to_courses[pre_course]:
                req_cnt_course[next_course] -= 1

                if req_cnt_course[next_course] == 0:
                    q.append(next_course)

        if len(order) == numCourses:
            return order
        return []
        