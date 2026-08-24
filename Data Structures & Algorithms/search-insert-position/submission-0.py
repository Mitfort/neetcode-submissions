class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n:int = len(nums)

        left,right = 0, n - 1

        while left <= right:
            mid:int = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if nums[mid] < target:
            return mid + 1
        
        return mid

            