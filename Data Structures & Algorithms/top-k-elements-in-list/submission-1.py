class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        box = []
        space = {}
        for i in range(len(nums)+1):
            box.append([])

        for num in nums:
            if num not in space:
                space[num] = 1
            else:
                space[num] += 1
        
        for num, c in space.items():
            box[c].append(num)

        result = []
        for i in range(len(box)-1,0,-1):
            for j in box[i]:
                result.append(j)
            if len(result) == k:
                 return result
        
       
