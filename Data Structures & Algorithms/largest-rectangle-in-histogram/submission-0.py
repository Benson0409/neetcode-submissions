class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        
        largest = 0

        heights.append(0)

        for n in range(len(heights)):
            
            
            while stack and heights[n] < heights[stack[-1]]:
                
                last = stack.pop()

                if stack:
                    width = n - stack[-1] -1 
                else:
                    width = n
                    
                largest = max(largest,width * heights[last])
                    
                

            stack.append(n)
            
                
        return largest