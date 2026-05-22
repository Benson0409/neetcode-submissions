class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        width = len(grid)
        high = len(grid[0])


        def dfs(row,col) -> int:
            if row < 0 or row >=width or col <0 or col>=high or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)     

        for i in range(width):
            for j in range(high):
                if grid[i][j] == 1:
                    max_island = max(dfs(i,j),max_island)

        return max_island