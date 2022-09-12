class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0
        for price in prices:
            diff = price - minBuy
            maxProfit = max(diff,maxProfit)
            minBuy = min(minBuy,price)
            
        return(maxProfit)        