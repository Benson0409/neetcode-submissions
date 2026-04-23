class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 1
        r = len(numbers)
        
        while l < r:
            if numbers[l-1] + numbers[r-1] > target:
                r -= 1
                continue
            if numbers[l-1] + numbers[r-1] < target:
                l +=1
                continue
            return [l,r]
            