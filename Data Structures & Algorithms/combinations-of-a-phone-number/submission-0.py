class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        data = {'2':["a","b","c"],'3':["d","e","f"],'4':["g","h","i"],
                '5':["j","k","l"],'6':["m","n","o"],'7':["p","q","r","s"],
                '8':["t","u","v"],'9':["w","x","y","z"]}


        answer = []

        def dfs(path,index):
            if index == len(digits):
                answer.append(path)
                return


            key = data[digits[index]]
            for n in key:
                dfs(path + n,index + 1)



        dfs("",0)
        return answer