class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxGains:int = 0 
        n:int = len(prices)
        l:int = 0
        profit:int = 0
        l_price:int = prices[l]

        for r in range(1,n):
            r_price:int = prices[r]

            profit = r_price - l_price

            if profit > maxGains:
                maxGains = profit

            if r_price < l_price:
                l = r
                l_price = r_price
            
        return maxGains 
