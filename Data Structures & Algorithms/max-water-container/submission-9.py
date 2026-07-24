class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n:int = len(heights)
        l,r = 0, n-1
        maxWater:int = 0

        while l < r:
            waterContained = (r - l) * min(heights[l],heights[r])
            if waterContained > maxWater:
                maxWater = waterContained
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxWater

            

