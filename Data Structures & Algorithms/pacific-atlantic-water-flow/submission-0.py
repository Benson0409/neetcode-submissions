class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        width = len(heights[0])
        high = len(heights)

        pacific = set()
        atlantic = set()

        pacific_bus = deque()
        atlantic_bus = deque()

        for i in range(high):
            for j in range(width):
                if i == 0 or j==0:
                    pacific_bus.append((i,j))
                    pacific.add((i,j))

                if j == width-1 or i == high-1:
                    atlantic_bus.append((i,j))
                    atlantic.add((i,j))

        direction = ((1,0),(-1,0),(0,1),(0,-1))
        while pacific_bus:
            long = len(pacific_bus)
            for i in range(long):
                current_h,current_w = pacific_bus.popleft()
                for h,v in direction:
                    nh = current_h + h
                    nv = current_w + v
                    if 0<= nh <high and 0<= nv <width and heights[nh][nv] >= heights[current_h][current_w]and(nh,nv) not in pacific:
                        pacific_bus.append((nh,nv))
                        pacific.add((nh,nv))
        
        while atlantic_bus:
        
            long = len(atlantic_bus)

            for i in range(long):
                current_h,current_w = atlantic_bus.popleft()
                for h,v in direction:
                    nh = current_h + h
                    nv = current_w + v
                    if 0<= nh <high and 0<= nv <width and heights[nh][nv] >= heights[current_h][current_w]and(nh,nv) not in atlantic:
                        atlantic_bus.append((nh,nv))
                        atlantic.add((nh,nv))


        return list(pacific & atlantic)
