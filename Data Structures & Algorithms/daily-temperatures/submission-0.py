class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # [30,38,30,36,35,40,28] 
        #. [0,1, ]

        # [0,1]
        # res =[]append(1-0)

        # [30, 31,31, 31] => [1,0,0,0]
        # [] => no
        # [5,5] =[0,0]
        
        # stack => collect index num
        # result len of temperatures, all element 0

        # loop through given list, 
    
        # for firt temp , stack append idx num
        # start compare current idx temp with stack last index temp,
        # if current temp > last index stack temp, 
        # update result current idx to differ  idx ofcurrent temp -idx last index
        # stack current temp id 
        # result 

        # time : O(n) space:O(n) 

        stack = []
        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            # i=0,
            # i=1,
            # i =3

            while stack and temperatures[stack[-1]] < temperatures[i]:
                
                diff = i - stack[-1] # 1-0=1
                result[stack[-1]] = i - stack[-1]
                stack.pop()# [1,0,0,....]
 
            stack.append(i) 
            # stack=[0,]
        return result















        