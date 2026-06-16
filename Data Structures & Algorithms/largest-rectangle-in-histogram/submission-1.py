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
        
        for i in range(len(heights)): 
        
            while stack and heights[i] < heights[stack[-1]]:
                # i = 0, stack= [0]
                # i = 1, stack= [0] heights[1](1)< heights[stack[-1]](7)
                # i = 2, stack= [1] heights[2](7)< heights[stack[-1]](1)
                # i = 3, stack= [1,2] heights[3](2)< heights[stack[-1]](7)
                # i = 3, stack= [1] heights[3](2)< heights[stack[-1]](7)
                # i = 4, stack= [1,3] heights[4](2)< heights[stack[-1]](2)
                

                
                
                height = heights[stack.pop()] 
                # i = 1, height =7, s=[] stack.pop() = 0
                # i = 3, height =7, s=[1] stack.pop() = 2
                
                if len(stack) == 0:
                    width = i 
                    # i =1, width = 1
                else:
                    width = i - stack[-1]-1 
                    # i =3, width = 3-1-1=1
                     

                max_area = max(max_area, height*width) # 7
            
            stack.append(i) 
            # i =1 , [1]
            # i =2 , [1,2]
            # i =3 , [1,3]
            
 
        return max_area 

        



        


        