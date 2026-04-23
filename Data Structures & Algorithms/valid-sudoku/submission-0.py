class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = collections.defaultdict(set)
        row = collections.defaultdict(set)
        column = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                current = board[i][j]

                if board[i][j] == ".":
                    continue
                
                box_id = (i//3,j//3)

                if current in box[box_id] or current in row[i] or current in column[j]:
                    return False
                
                box[box_id].add(current)
                row[i].add(current)
                column[j].add(current)


        return True
             