class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxLength = 0
        for i in nums:
            if i-1 not in num_set:
                currentLength = 1
                currentNum = i
                while currentNum+1 in num_set:
                    currentLength +=1
                    currentNum += 1
                if maxLength<currentLength:
                     maxLength = currentLength
                # maxLength = lambda:maxLength<currentLength,currentLength

        return maxLength
