class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_h = float("inf")
        k = 0
        left = 1
        right = max(piles)
        

        if h == right:
            return max(piles)

        while left <= right:

            mid = (right + left) // 2
            hour = 0

            for pile in piles:
                if pile % mid !=0:
                    hour += (pile//mid) + 1
                else:
                    hour += (pile//mid)

            if hour > h:
                left = mid + 1
            else:
                
                k = mid
                right = mid -1

        return k
            

        
        