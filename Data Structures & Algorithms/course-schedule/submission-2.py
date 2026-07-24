class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build graph: key is pre_course, value is list of course
        # Buold list: i is course, list[i] is how many pre_course should take before course list[i]
        # deque store if the course doesn't need to take precourse => if list[i] == 0
        # while loop deque, pop from deque, finish course +1, 
        # loop through next courses of this finished course in graph, decrease next course by 1 in list, it means,
        # for taking this course, already finish one pre course
        # if this course in list is 0 , if it doesn't need to take pre course, append it to deque,
        # return a boolean if finished course is eqaul to numCourses

        graph = defaultdict(list)
        indegree = [0] * numCourses 

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0

        while queue:

            pre_course = queue.popleft() 
            completed += 1 

            for next_course in graph[pre_course]: 

                indegree[next_course] -= 1 

                if indegree[next_course] == 0:
                    queue.append(next_course) 
        return completed == numCourses