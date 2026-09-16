class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n:int = len(nums)

        def backtrack(i,arr):
            if i >= n:
                res.append(arr.copy())
                return
            
            for j in range(0,n):
                if nums[j] in arr:
                    continue

                arr.append(nums[j])
                backtrack(i+1,arr)
                arr.pop() 
        
        backtrack(0,[])

        return res


            
