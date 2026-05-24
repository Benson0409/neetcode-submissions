class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        empty = 2147483647
        width = len(grid[0])
        high = len(grid)
        run = 0
        bus = deque()


        for i in range(high):
            for n in range(width):
                if grid[i][n] == 0:
                    bus.append((i,n))

        while bus:
            long = len(bus)
            run += 1
            for i in range(long):
                current = bus.popleft()
                current_h = current[0]
                current_w = current[1]

                if 0 <= current_h - 1 < high and 0 <= current_w < width and grid[current_h - 1][current_w] == empty:
                    grid[current_h - 1][current_w] = run
                    bus.append((current_h - 1, current_w))

               
                if 0 <= current_h + 1 < high and 0 <= current_w < width and grid[current_h + 1][current_w] == empty:
                    grid[current_h + 1][current_w] = run
                    bus.append((current_h + 1, current_w))

                
                if 0 <= current_h < high and 0 <= current_w - 1 < width and grid[current_h][current_w - 1] == empty:
                    grid[current_h][current_w - 1] = run
                    bus.append((current_h, current_w - 1))

                
                if 0 <= current_h < high and 0 <= current_w + 1 < width and grid[current_h][current_w + 1] == empty:
                    grid[current_h][current_w + 1] = run
                    bus.append((current_h, current_w + 1))
                





        
