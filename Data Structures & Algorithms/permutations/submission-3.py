class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(path):
            if len(path) == len(nums):
                answer.append(path)
                return

            for i in nums:
                if i in path:
                    continue
                dfs(path+[i])

        dfs([])
        return answer
