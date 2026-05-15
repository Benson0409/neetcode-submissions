class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(nums)
        self.k = k

        while len(nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val) 

        elif val > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)

        return self.nums[0]
        
            
