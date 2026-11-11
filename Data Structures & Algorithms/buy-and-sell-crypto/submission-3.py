class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxGain:int = 0
        minBuy:int = prices[0]

        for sell in prices:
            maxGain = max(maxGain, sell - minBuy)
            minBuy = min(minBuy, sell)
            
        return maxGain


