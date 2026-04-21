class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        box = []
        space = {}
        box = [[]for i in range(len(nums)+1)]

        for num in nums:
            space[num] = 1 + space.get(num, 0)
        
        for num, c in space.items():
            box[c].append(num)

        result = []
        for i in range(len(box)-1,0,-1):
            for j in box[i]:
                result.append(j)
                if len(result) == k:
                 return result
        
       
