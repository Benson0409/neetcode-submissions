class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        for i in nums:
            temp = []
            for n in answer:
                new = n + [i]
                temp.append(new)
            answer.extend(temp)
        return answer        
