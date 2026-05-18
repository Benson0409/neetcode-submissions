class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(path,current):
            if len(path) == len(nums):
                answer.append(path)

            for i in range(len(nums)):
                if i in current:
                    continue
                dfs(path+[nums[i]],current + [i])

        dfs([],[])
        return answer
