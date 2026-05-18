class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        nums = sorted(candidates)
        def dfs(index,path,num):
            if num == 0:
                answer.append(path)
                return
            if len(nums) == index or num < 0:
                return

            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path + [nums[i]],num - nums[i])

        dfs(0,[],target)
        return answer