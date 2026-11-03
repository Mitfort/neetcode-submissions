class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter:dict[int,int] = {}

        for n in nums:
            if counter.get(n, 0) > 0:
                return True
            
            else:
                counter[n] = 1

        return False