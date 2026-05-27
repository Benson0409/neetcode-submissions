class Solution:
    def solve(self, board: List[List[str]]) -> None:
        width = len(board[0])
        high = len(board)
        
        direction = ((1,0),(-1,0),(0,1),(0,-1))

        def dfs(col,row):
            if board[col][row] == "X":
                return
            board[col][row] = "T"

            for h,v in direction:
                nh = col + h
                nv = row + v

                if 0<= nh < high and 0 <= nv <width and board[nh][nv]=="O":
                    dfs(nh,nv)
            

        for i in range(high):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][width - 1] == "O":
                dfs(i, width - 1)

        for j in range(width):
            if board[0][j] == "O":
                dfs(0, j)
            if board[high - 1][j] == "O":
                dfs(high - 1, j)


        for i in range(high):
            for j in range(width):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
            
