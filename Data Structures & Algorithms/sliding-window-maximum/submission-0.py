class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        
        max_num = []
        for i in range(len(nums) - k+1):
            current = []
            for n in range(i,i+k):
                current.append(nums[n])
            max_num.append(max(current))

        return max_num
            
            
