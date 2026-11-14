class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n:int = len(nums)
        res = []

        for i in range(n):
            l = i+1
            r = n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    ls = [nums[i], nums[l], nums[r]]

                    if ls not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    l+=1
                elif s < 0:
                    l+=1 
                else:
                    r-=1 

        return res
                
