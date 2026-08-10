class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build an adjacency list, compute pre crs for each crs
        # Initialize a queue with all courses having pre crs 0
        # for pre crs, add the its nxt course and all its prerequisites to the successor's prerequisite set
        # Decrement the successor's indegree and add to queue if it becomes
        # After processing all courses, each course has a complete set of its prerequisites
        # for each query (u, v), check if u is in the prerequisite set of v
        # time:O(V*(V+E)+m), space:O(V*V+E+m)
        # v:numCourses, E:num of prerequisites, m:len(queries)
        adj = [set() for _ in range(numCourses)]
        isPrereq = [set() for _ in range(numCourses)]
        count_pres = [0] * numCourses

        for pre_crs, nxt_crs in prerequisites:
            adj[pre_crs].add(nxt_crs)
            count_pres[nxt_crs] += 1

        q = deque()
        for crs in range(numCourses):
            if count_pres[crs] == 0:
                q.append(crs)

        while q:
            pre_crs = q.popleft()
            for nxt_crs in adj[pre_crs]:
                isPrereq[nxt_crs].add(pre_crs)
                isPrereq[nxt_crs].update(
                    isPrereq[pre_crs]
                )
                count_pres[nxt_crs] -= 1
                if count_pres[nxt_crs] == 0:
                    q.append(nxt_crs)

        return [u in isPrereq[v] for u, v in queries]
                

        



        