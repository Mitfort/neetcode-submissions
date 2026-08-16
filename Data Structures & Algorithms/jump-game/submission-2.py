class Solution:
    def canJump(self, nums: List[int]) -> bool:
        destinationIdx = len(nums) - 1
        
        for idx in range(destinationIdx, -1, -1):
            if idx + nums[idx] >= destinationIdx:
                destinationIdx = idx
        
        return True if destinationIdx == 0 else False