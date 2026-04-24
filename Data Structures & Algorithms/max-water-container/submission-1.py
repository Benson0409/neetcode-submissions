class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        answer = 0
        for i in range(len(heights)):
            r = len(heights)
            l = 1+i
            while l<r:
                current = min(heights[l-1],heights[r-1])*(r-l)
                if current > answer:
                    answer = current
                if heights[l-1] < heights[r-1]:
                    l += 1
                else:
                    r -= 1

        return answer
