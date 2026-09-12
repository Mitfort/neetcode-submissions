class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res:List[int] = set()
        n:int = len(nums)

        counter = {}

        for i in nums:
            counter[i] = counter.get(i,0) + 1

            if counter[i] > n / 3:
                res.add(i)

        return list(res)