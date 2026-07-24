class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n: int = len(nums)
        res = [] 

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            l,r = i+1, n - 1

            while l < r:
                suma = num + nums[l] + nums[r]

                if suma > 0:
                    r -= 1
                elif suma < 0:
                    l += 1
                else:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return res