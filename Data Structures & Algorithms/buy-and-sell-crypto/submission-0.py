class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf: int = 0
        n: int = len(prices)

        for i in range(n): # the buy index
            for j in range(i, n): # the sell index
                profit:int = prices[j] - prices[i]

                if profit > maxProf:
                    maxProf = profit

        return maxProf  
            



        