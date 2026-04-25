class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = 0
        max_sale = 0
        n = 1
        for i in range(len(prices)):
            
            current = prices[i]
            
            for n in range(i+1,len(prices)):
                max_sale = max(max_sale,prices[n]-current)
        return max_sale
