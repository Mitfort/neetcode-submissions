class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 0, n

        while l<=r:
            mid = (l+r)//2
            coins = mid * (mid + 1) // 2

            if coins > n:
                r = mid - 1
            else:
                l = mid + 1

        return r
            


        # coins:List[int] = [0 for i in range(n+1)]

        # for i in range(1,n+1):
        #     coins[i] = coins[i-1] + i

        # l,r = 0, n - 1
        
        # while l <= r:
        #     mid = (l + r) // 2

        #     if coins[mid] < n:
        #         l = mid + 1
        #     elif coins[mid] > n:
        #         r = mid - 1
        #     else:
        #         return mid

        # if coins[mid] > n:
        #     return mid - 1
        
        # return mid
