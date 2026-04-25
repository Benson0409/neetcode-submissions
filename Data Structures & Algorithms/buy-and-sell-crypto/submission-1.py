class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_sell = 0
       
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])

            max_sell = max(max_sell,prices[i] - min_price)
            
        return max_sell
