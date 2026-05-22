class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        width = len(grid)
        high = len(grid[0])

        def dfs(row,col):

            grid[row][col] = '0'

            if row + 1 < width and grid[row+1][col] == '1':
                dfs(row+1, col)
            if row - 1 >= 0 and grid[row-1][col] == '1':
                dfs(row-1, col)
            if col + 1 < high and grid[row][col+1] == '1':
                dfs(row, col+1)
            if col - 1 >= 0 and grid[row][col-1] == '1':
                dfs(row, col-1)



        for i in range(width):
            for j in range(high):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i,j)

        return island 
            