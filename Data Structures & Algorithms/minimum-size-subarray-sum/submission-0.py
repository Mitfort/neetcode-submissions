class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        l:int = 0
        currSum:int = 0

        for r in range(len(nums)):
            currSum += nums[r]

            while currSum >= target:
                length = r - l + 1

                if length < minLen:
                    minLen = length

                currSum -= nums[l]
                l+=1   
                    
        if minLen == float('inf'):
            return 0 

        return minLen