class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maybe n >= len(tasks)
        # all are uppercase Eng letters
        # one task one uppercase Eng letter

        # store every task frequency, use hashmap, key is task, value is freq
        # tasks = ["A","A","A","B","B""C"] 
        # [-3,-2,-1]
        # deque = [(realease_time, count)]
        # -3+1=-2, 0+1+n 

        # need to run most freq task first, heap, max heap, [-count]
        # we can store, task release time and the current task count in deque
        # initial time is 0
        # while loop,
        # time icrease by 1
        # if heap, we can know the most tasks number,heap pop +1
        # if after running , if the curent task count is not zero
        # deque should append the curent task count and time + n
        # we neede check if the deque is not empty and first task time + n  is eqaul to time
        # pop the count of this task , put it in to heap
        # return time

        # time: O(n)=> n len tasks, space: O(1) = 26letters
# Input: tasks = ["A","A","A","B","C"], n = 3
        freq = Counter(tasks) #{"A":3,"B":1,"C:1"}
        heap = [-c for c in freq.values()]
        heapq.heapify(heap)
        # heap [-3,-1,-1]
        cooldown = deque()
        time = 0
        while heap or cooldown:
            time += 1 #1,2,3,4,5,6,7,8,9

            if heap:
                cnt = heapq.heappop(heap) + 1 #cnt =-2,-1+1=0,-1+1=0,-1 -1+1=0

                if cnt:
                    cooldown.append((time + n, cnt)) #[(4,-2)] [(8,-1)]
            
            if cooldown and cooldown[0][0] == time: #4!=1 #4!=2,#4!=3#4==4
            # 8!=5, #8!=6 #8!=7 #8==8
                _, count = cooldown.popleft() #4,-2, #(8,-1)
                heapq.heappush(heap, count) #heap=[-2]#heap=[--1]

        return time#9



            
 

        
        