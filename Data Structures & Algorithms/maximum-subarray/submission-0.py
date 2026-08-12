class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        for n in nums[1:]:
            currSum = max(currSum, 0)
            currSum += n
            maxSum = max(maxSum, currSum)    
        
        return maxSum