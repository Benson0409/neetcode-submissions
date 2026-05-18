class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(index,path):
            if index == len(nums):
                answer.append(path)
                return

            dfs(index+1,path)
            dfs(index+1,path + [nums[index]])

        dfs(0,[])
        return answer

            

        