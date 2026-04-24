class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left_max = 0
        right_max = 0

        
        l = 0
        r = len(height) - 1

        while l < r:
            
            if height[l] > left_max:
                left_max = height[l]
            if height[r] > right_max:
                right_max = height[r]

            
            if left_max < right_max:
               
                answer += (left_max - height[l])
                l += 1  
            else:
               
                answer += (right_max - height[r])
                r -= 1  

        return answer