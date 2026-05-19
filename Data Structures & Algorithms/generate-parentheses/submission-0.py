class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
        answer = []


        def dfs(path,left_num,right_num):
            if right_num == 0 and left_num ==0:
                answer.append(path)
                return

           
            if left_num > 0:
                dfs(path+"(",left_num-1,right_num)
            if right_num > left_num:
                dfs(path+")",left_num,right_num-1)

        dfs("",n,n)
        return answer