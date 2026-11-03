class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # dict for containing missing,index
        rests:dict[int,int] = {}

        for i,n in enumerate(nums):
            missing = target - n
            rests[missing] = i

        for j,n in enumerate(nums):
            if rests.get(n,0):
                i = rests[n]

                if i != j:
                    return [j,i]

        return [] 

