class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res:int = 1
        n:int = len(nums)

        maxLen:list[int] = [1] * n

        for i in range(1,n):
            curr = maxLen[i]

            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    maxLen[i] = max(maxLen[i], maxLen[j] + 1)
            
            res = max(res,maxLen[i])
        
        return res
        