class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = {}
        for i,num in enumerate(nums):
            if num not in answer:
                answer[num] = 1
            else:
                answer[num] += 1
        sort_key = sorted(answer.items(),key = lambda  x : x[1],reverse=True)
        
        result = []
        for i in range(k):
            result.append(sort_key[i][0])
            
        return result
       
