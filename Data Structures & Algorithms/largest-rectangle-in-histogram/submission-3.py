class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):

            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                
                height = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    # (i-1) - (stack[-1] + 1) + 1
                    width = i - stack[-1] - 1
                    
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea
        