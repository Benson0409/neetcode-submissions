class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number = set(numbers)
        for i in numbers:
            diff = target - i
            if diff in number and diff != i:
                return [numbers.index(i)+1,numbers.index(diff)+1]