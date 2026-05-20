class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def dfs(index,path):
            if index == len(s):
                answer.append(path)
                return

            for i in range(index,len(s)):
                substring = s[index:i+1]

                if substring == substring[::-1]:
                    dfs(i+1,path+[substring])



        dfs(0,[])
        return answer
        