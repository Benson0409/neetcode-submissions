class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def dfs(index,path,num):
            
            if num == 0:
                answer.append(path)
                return

            if num < 0:
                return

            for i in range(index,len(nums)):
                dfs(i,path+[nums[i]],num-nums[i])

        dfs(0,[],target)
        return answer
