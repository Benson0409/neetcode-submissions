class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        heap = []
        task_dict = {}
        cold = deque()

        for i in tasks:
            task_dict[i] = task_dict.get(i,0) + 1
        
        for i in task_dict.values():
            heap.append(-i)

        heapq.heapify(heap)

        while heap or cold:
            time += 1
            if heap:
                current = heapq.heappop(heap)
                current += 1

                if current < 0: 
                    cold_time = n + time
                    cold.append((current,cold_time))

            if cold and cold[0][1] == time:
                released = cold.popleft()
                heapq.heappush(heap,released[0])

        return time
            




        

            
