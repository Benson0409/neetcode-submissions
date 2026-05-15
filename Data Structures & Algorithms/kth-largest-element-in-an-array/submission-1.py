class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            heapq.heappush(heap,-i)
        for i in range(len(heap)):
            if i == k-1:
                return -(heapq.heappop(heap))
            heapq.heappop(heap)