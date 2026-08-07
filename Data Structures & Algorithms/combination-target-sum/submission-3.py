class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        subset = []

        def backtrack(i, arr, currSum):
            if i >= len(nums) or currSum > target:
                return

            
            if currSum == target:
                res.append(arr.copy())
                return

            currSum += nums[i]
            arr.append(nums[i])

            backtrack(i, arr, currSum)
            arr.pop()
            backtrack(i+1, arr, currSum - nums[i])
            
        backtrack(0,[],0)

        return res