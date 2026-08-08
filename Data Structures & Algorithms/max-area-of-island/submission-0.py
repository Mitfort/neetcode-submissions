class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0 

        ROWS,COLS = len(grid), len(grid[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    continue
                
                q = collections.deque([(i,j)])
                area = 0

                while q:
                    row,col = q.pop()
                    
                    if grid[row][col] == 0:
                        continue
                    
                    area+=1
                    grid[row][col] = 0

                    if row > 0:
                        q.append((row-1,col))

                    if row < ROWS - 1:
                        q.append((row+1,col))

                    if col > 0:
                        q.append((row,col-1))

                    if col < COLS - 1:
                        q.append((row,col+1))
                    

                maxArea = max(area,maxArea)




        return maxArea