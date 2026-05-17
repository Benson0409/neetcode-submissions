class MedianFinder:

    def __init__(self):
        self.right = []
        self.left = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)

        val = -heapq.heappop(self.left)
        heapq.heappush(self.right,val)

        if len(self.left)+1 < len(self.right):
            num = -heapq.heappop(self.right)
            heapq.heappush(self.left,num)
        

    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return float(self.right[0])
            
        return (self.right[0] - self.left[0]) / 2.0

        