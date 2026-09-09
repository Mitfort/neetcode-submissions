class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 and col == 0: continue 

                if row == 0 and col - 1 >= 0:
                    grid[row][col] += grid[row][col - 1]
                    continue
                
                if col - 1 >= 0:
                    grid[row][col] += min(grid[row][col-1],grid[row-1][col])
                else:
                    grid[row][col] += grid[row-1][col]

        return grid[-1][-1]
