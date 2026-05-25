class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        high = len(grid)
        run = -1
        fruit = 0
        bus = deque()

        for i in range(high):
            for j in range(width):
                if grid[i][j] == 2:
                    bus.append((i,j))
                elif grid[i][j] == 1:
                    fruit += 1


        if fruit ==0:
            return 0


        while bus:
            long = len(bus)
            run += 1
            direction = ((1,0),(-1,0),(0,1),(0,-1))

            for i in range(long):
                current_h,current_w = bus.popleft()

                for v,h in direction:
                    nv = current_w + v
                    nh = current_h + h

                    if 0<=nv<width and 0<=nh<high and grid[nh][nv] == 1:
                        grid[nh][nv] = 2
                        fruit -= 1
                        bus.append((nh,nv))


        if fruit > 0:
            return -1
            
        return run
