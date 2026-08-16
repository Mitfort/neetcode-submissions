class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        if amount < min(coins):
            return -1

        q = deque([0])

        seen = [False] * (amount + 1)
        seen[0] = True

        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return res
                    
                    if nxt > amount or seen[nxt]:
                        continue
                    
                    seen[nxt] = True
                    q.append(nxt)
        return -1

        # self.minCounter:int = amount;

        # def selectCoin(currSum:int, counter:int):
        #     if currSum > amount or counter > self.minCounter:
        #         return 

        #     for coin in coins:
        #         if currSum + coin > amount:
        #             continue
                
        #         if currSum + coin == amount:
        #             self.minCounter = min(counter,self.minCounter)
        #             return 
        #         else:
        #             selectCoin(currSum+coin,counter+1)

        # selectCoin(0,0)

        # if 1 not in coins and self.minCounter == amount:
        #     return -1

        # return self.minCounter + 1
                