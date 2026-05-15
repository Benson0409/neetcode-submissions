class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        answer = []
        for i in points:
            x = i[0]**2 + i[1]**2
            
            distance.append((x,i))

        
        heapq.heapify(distance)
        
        for i in range(k):
            min_distance = heapq.heappop(distance)
            answer.append(min_distance[1])

        return answer
        