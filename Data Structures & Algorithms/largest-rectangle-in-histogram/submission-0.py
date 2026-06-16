class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # [7,1,7,2,2,4]
        #  ^ => heigh = 7, every two idx distance 1 
        #  7,1 => area = heigh * width = max(7,1) * 1 = 7

        # 1 <= heights.length <= 1000.
        # 0 <= heights[i] <= 1000
        # [7,7,7,7] => heigh = 7 , (4-0) = 28
        # [7] => 7
        # input always is valid
        # time: O(n), space: O(n)

        # max area start with 0
        max_area  = 0
        # stack alway collect index number [0]
        stack = []
        heights.append(0)
        
        for i in range(len(heights)): #i=0,i=1,i=2,i=3, i= 4, i =5 i =6
        
            while stack and heights[i] < heights[stack[-1]]:# 
                # stack heights[1]=1 < heights[0]=7 T
                # stack heights[2]=7 < heights[1]=1 F
                # stack heights[3]=2 < heights[2]=7 T 
                # stack heights[3]=2 < heights[1]=1 F 
                # stack heights[4]=2 < heights[3]=2 F 
                # stack heights[5]=4 < heights[4]=2 F 
                # stack heights[6]=0 < heights[5]=4 F 
                # stack heights[6]=0 < heights[4]=2 F 
                # stack heights[6]=0 < heights[3]=2 F 
                # stack heights[6]=0 < heights[1]=1 F 

            
                height = heights[stack.pop()] 
                # 7, s=[] stack.pop() = 0
                # 7, s=[1] stack.pop() = 2
                # 4, s =[1,3,4], stack.pop() = 5
                # 2, s =[1,3], stack.pop() = 4
                # 2, s =[1], stack.pop() = 3
                # 1, s =[], stack.pop() = 1


                if len(stack) == 0:
                    width = i # width= 1,6
                else:
                    width = i - stack[-1]-1 # 3-1-1=1# 6-4-1=1, 6-3-1=2, 6-1-1=4

                max_area = max(max_area, height*width) # 8
            
            stack.append(i) # [1,3,4,5]
 
        return max_area 

        



        


        