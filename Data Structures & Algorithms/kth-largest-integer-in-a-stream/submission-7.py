class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse=True)[:k]
        self.k = k

    def add(self, val: int) -> int:
        instered = False
        for i in range(len(self.nums)):
            if self.nums[i]<val:
                self.nums.insert(i,val)
                instered = True
                break

        if instered is False:
            self.nums.append(val)
          
        
        if len(self.nums) > self.k:
            self.nums.pop()

        return self.nums[-1]
        
            
