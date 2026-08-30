class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = 0,0 
        n = len(weights)

        for i in range(n):
            if weights[i] > l:
                l = weights[i]

            r += weights[i]

        res = r

        while l <= r:
            mid = (l + r) // 2

            n_ships = 1
            curr = 0

            for i in range(n):
                if curr + weights[i] > mid:
                    n_ships += 1
                    curr = 0

                curr += weights[i]

                
            if n_ships <= days:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res

