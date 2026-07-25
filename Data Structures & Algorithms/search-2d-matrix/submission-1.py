class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:
                continue
            else:
                return self.searchRow(row,target)

        return False
    
    def searchRow(self, row: List[int], target:int) -> bool:
        l,r = 0, len(row) - 1

        while l <= r:
            mid = (l + r) // 2

            if row[mid] < target:
                l = mid+1
            elif row[mid] > target:
                r = mid - 1
            else:
                return True
        
        return False