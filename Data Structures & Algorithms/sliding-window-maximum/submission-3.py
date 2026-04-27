class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      
        max_num = []
        current = []
        num_dict = {}
        l = 0
        for i in range(len(nums)):
            num_dict[nums[i]] = num_dict.get(nums[i],0)+1
            if i+1 >= k:
                max_num.append(max(num_dict))

                
                num_dict[nums[l]] -= 1
                if num_dict[nums[l]] == 0:
                    num_dict.pop(nums[l])
                l += 1

        return max_num
            
            
