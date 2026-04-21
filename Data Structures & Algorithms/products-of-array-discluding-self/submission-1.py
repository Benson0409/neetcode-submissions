class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_box = []
        right_box = [1] * len(nums)

        for i in range(len(nums)):
            diff = len(nums) - i

            if i == 0:
                left_box.append(1)
                continue
            
            left_box.append(left_box[i-1]*nums[i-1])
        
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums) - 1:
                right_box[i] = 1
                continue
            right_box[i] = right_box[i+1]*nums[i+1]
        print(right_box)
        
        answer = []
        for i in range(len(nums)):
            answer.append(right_box[i] * left_box[i])

        return answer

