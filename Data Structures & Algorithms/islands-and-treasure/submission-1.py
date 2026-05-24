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
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for dh, dw in directions:
                    
                    
                    next_h = current_h + dh
                    next_w = current_w + dw

            
                    if 0 <= next_h < high and 0 <= next_w < width and grid[next_h][next_w] == empty:
                        
                        grid[next_h][next_w] = run
                        bus.append((next_h, next_w))





        
