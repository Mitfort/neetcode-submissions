class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res:List[List[int]] = []
        n:int = len(nums)
        nums.sort()

        def backtrack(idx,vals):
            s = sum(vals)
            
            for i in range(idx,n):
                n_num = nums[i]

                if s + n_num == target: 
                    self.res.append([*vals,n_num])
                    continue 
                elif s + n_num < target: 
                    backtrack(i,[*vals,n_num])
                    continue
                else:
                    break
        
        backtrack(0,[])

        return self.res
                