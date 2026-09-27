class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n:int = len(nums)
        pre:List[int] = [1] * n
        suf:List[int] = [1] * n

        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]

        for j in range(n-2, -1, -1):
            suf[j] = suf[j+1] * nums[j+1]
        
        return [pre[i] * suf[i] for i in range(n)]