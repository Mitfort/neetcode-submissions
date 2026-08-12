class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            x,y = -heapq.heappop(stones), -heapq.heappop(stones)

            if x == y:
                continue

            z = max(x,y) - min(x,y)

            heapq.heappush(stones,-z)
        
        if stones:
            return -stones[0]

        return 0  

            

            

