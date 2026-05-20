class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(path,row,column):
            if path == len(word):
                return True
            if (row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] != word[path]):
                return False

            temp = board[row][column]
            board[row][column] = "#"

            result = dfs(path+1,row+1,column) or dfs(path+1,row-1,column) or dfs(path+1,row,column-1) or dfs(path+1,row,column+1)

            board[row][column] = temp
            
            return result

        for i in range(len(board)):
            for n in range(len(board[0])):
                if board[i][n] == word[0]:
                    if dfs(0,i,n):
                        return True

        return False