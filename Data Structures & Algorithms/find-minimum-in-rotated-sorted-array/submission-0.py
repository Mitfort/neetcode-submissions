class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums) - 1

        minimum = nums[l]

        while l <= r: 
            if nums[r] < minimum: 
                minimum = nums[r]
            
            if nums[r] < nums[l]:
                l+=1
            else:
                r-=1

            if nums[l] < minimum:
                minimum = nums[l]
        
        return minimum

            
            