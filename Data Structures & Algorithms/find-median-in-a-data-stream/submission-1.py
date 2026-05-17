class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        clear_nums = sorted(self.nums)
        mid = len(clear_nums) // 2
        
        if len(clear_nums) % 2 != 0:
            return float(clear_nums[mid])

        else:
            return (float(clear_nums[mid-1]) + float(clear_nums[mid]))/2

        