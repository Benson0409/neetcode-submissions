class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def isSubstring(left,right)->bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(index,path):
            if index == len(s):
                answer.append(path)
                return

            for i in range(index,len(s)):

                if isSubstring(index,i):
                    dfs(i + 1, path + [s[index:i+1]])

        dfs(0,[])
        return answer
        