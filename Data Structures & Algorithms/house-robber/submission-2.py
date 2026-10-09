class Solution:
    def rob(self, nums: List[int]) -> int:
        n:int = len(nums)
        money:List[int] = [0] * (n+1)
        money[1] = nums[0]

        for i in range(2,n+1):
            money[i] = max(money[i-1], nums[i-1] + money[i-2])

        print(money)

        return money[-1]
