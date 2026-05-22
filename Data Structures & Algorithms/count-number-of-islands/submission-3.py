class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        width = len(grid)
        high = len(grid[0])

        def dfs(row,col):
            
            if row < 0 or row >= width or col < 0 or col >= high or grid[row][col] == '0' :
                return


            grid[row][col] = '0'

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)



        for i in range(width):
            for j in range(high):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i,j)

        return island 
            