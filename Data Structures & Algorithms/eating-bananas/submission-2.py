class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        

        if h == right:
            return max(piles)

        while left <= right:

            mid = (right + left) // 2
            hour = 0
            for pile in piles:
                hour += (pile + mid -1) // mid 

            if hour > h:
                left = mid + 1
            else:
                right = mid -1

        return left
            

        
        