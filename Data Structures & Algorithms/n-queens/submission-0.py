class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_digi = set()
        neg_digi = set()

        board = []
        answer = []
        
        for _ in range(n):
            board.append(["."] * n)

        
        def dfs(row):
            if row == n:
                data = []
                for r in board:
                    data.append("".join(r))

                answer.append(data)
                return


            for col in range(n):
                if col in cols or (col+row) in pos_digi or (col-row) in (neg_digi):
                    continue
                board[row][col] = "Q"

                cols.add(col)
                pos_digi.add(col+row)
                neg_digi.add(col-row)

                dfs(row+1)

                board[row][col] = "."
                cols.remove(col)
                pos_digi.remove(col+row)
                neg_digi.remove(col-row)

        dfs(0)

        return answer


            
                

            


        