class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def dfs(index,path,num):
            
            if num == 0:
                answer.append(path)
                return

            if index == len(nums) or num < 0:
                return

            dfs(index,path+[nums[index]],num-nums[index])
            dfs(index+1,path,num)
        dfs(0,[],target)
        return answer
