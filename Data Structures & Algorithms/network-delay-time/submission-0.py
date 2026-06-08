class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        net = defaultdict(list)

        for i in times:
            net[i[0]].append((i[2],i[1]))

        
        max_time = 0 
        pq = [(0,k)]
        visited = set()

        while pq:
            current_time,value = heapq.heappop(pq)
            if value in visited:
                continue

            visited.add(value)

            max_time = max(max_time,current_time)

            for time,next_value in net[value]:
                if next_value not in visited:
                    heapq.heappush(pq, (current_time + time, next_value))

        if len(visited) == n:
            return max_time
        return -1
                



