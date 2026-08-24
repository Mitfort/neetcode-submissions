class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic:dict[int|int] = {}
        maxCounter:int = 0
        maxNum:int = 0
        half:int = len(nums) // 2

        for i in range(len(nums)):
            num = nums[i]
            dic[num] = dic.get(num,0) + 1

            if dic[num] > maxCounter:
                maxNum = num
                maxCounter = dic[num]

                if maxCounter > half:
                    return maxNum
        
        return maxNum

            
        