class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        for i in range(len(nums)):

            if i == 0:
                answer[i] = 1
                continue
            answer[i] = answer[i-1]*nums[i-1]
        
        r = 1
        for i in range(len(nums)-1, -1, -1):
                
            answer[i] = answer[i] * r
                
            r = r * nums[i] 
                
        return answer
        
      
    
