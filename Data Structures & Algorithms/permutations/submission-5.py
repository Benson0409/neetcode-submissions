class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        user = len(nums) * [False]
        def dfs(path):
            if len(path) == len(nums):
                answer.append(path)
                return

            for i in range(len(nums)):
                if user[i]:
                    continue
                user[i] = True
                dfs(path+[nums[i]])
                user[i] = False

        dfs([])
        return answer
