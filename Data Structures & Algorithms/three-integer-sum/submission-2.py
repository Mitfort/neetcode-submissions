class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n:int = len(nums)
        res:List[List[int]] = []

        if n <= 2: return []

        for i in range(n):
            target = nums[i]
            j, k = i+1, n - 1

            while j < k:
                add = target + nums[j] + nums[k]

                if add == 0 and [target,nums[j],nums[k]] not in res:
                    res.append([target,nums[j],nums[k]])
                elif add < 0:
                    j+=1
                else:
                    k-=1
                
        return res
                    
