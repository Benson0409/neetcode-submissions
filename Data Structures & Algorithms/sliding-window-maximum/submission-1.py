class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      
        max_num = []
        current = []

        for i in range(len(nums)):
            current.append(nums[i])
            if len(current) == k:
                max_num.append(max(current))
                del current[0]

        return max_num
            
            
