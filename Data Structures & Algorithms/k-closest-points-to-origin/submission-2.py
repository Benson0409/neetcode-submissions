class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        answer = []

        for i in points:
            x = i[0]**2 + i[1]**2
            heapq.heappush(distance,(-x,i))
            if len(distance) > k:
                heapq.heappop(distance)

        for i in distance:
            answer.append(i[1])
        
        return answer
        