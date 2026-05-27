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
            for j in range(width):
                if (i==0 or i == high-1 or j==0 or j==width-1) and board[i][j] == "O" :
                    dfs(i,j)


        for i in range(high):
            for j in range(width):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
            
