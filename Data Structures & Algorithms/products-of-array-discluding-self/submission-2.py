class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n:int = len(nums) 
        prefix:List[int] = [1] * n
        suffix:List[int] = [1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        res:List[int] = [0] * n

        for i in range(n):
            res[i] = suffix[i] * prefix[i]

        return res