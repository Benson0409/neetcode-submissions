class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_stones = []

        for i in stones:
            min_stones.append(-i)

        heapq.heapify(min_stones)

        while len(min_stones) > 1:
            x_stone = heapq.heappop(min_stones)
            y_stone = heapq.heappop(min_stones)

            dif = abs(x_stone - y_stone)
            if dif > 0:
                heapq.heappush(min_stones,-dif)
            

        if len(min_stones) == 1:
            return abs(min_stones[0])
        else:
            return 0

