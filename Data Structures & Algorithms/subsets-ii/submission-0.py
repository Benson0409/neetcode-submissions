class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        clear_nums = sorted(nums)
        answer = []

        def dfs(path,current):
            answer.append(path)

            for i in range(current,len(nums)):
                if i > current and clear_nums[i] == clear_nums[i-1]:
                    continue
            
                dfs(path+[clear_nums[i]],i+1)

        dfs([],0)
        return answer