class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        space = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in space:
                return [space[diff],i]
            space[num] = i