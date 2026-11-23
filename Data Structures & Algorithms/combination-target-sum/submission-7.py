class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return []
        res:List[List[int]] = []

        nums.sort()

        def backtrack(idx,arr,total):
            if total == target:
                res.append(arr.copy())
                return
            
            for j in range(idx, len(nums)):
                if total + nums[j] > target:
                    return 
                
                arr.append(nums[j])
                backtrack(j, arr, total + nums[j])
                arr.pop()

        backtrack(0,[],0)

        return res 