class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = n - 1
        forward = [1] * n 
        backward = [1] * n
        res = [1] * n

        forward[0] = nums[0]
        backward[-1] = nums[-1]

        for i in range(1,n-1):
            j-=1
            forward[i] = nums[i] * forward[i-1]
            backward[j] = nums[j] * backward[j+1]

        forward[-1] = nums[-1] * forward[n-2]
        backward[0] = nums[0] * backward[1]

        res[0] = backward[1]
        res[-1] = forward[n-2]
        
        for i in range(1,n-1):
            res[i] = forward[i-1] * backward[i+1]

        return res

        
        
