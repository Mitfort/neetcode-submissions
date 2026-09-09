class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS,COLS = len(obstacleGrid), len(obstacleGrid[0])

        paths:List[int] = [0] * COLS
        paths[0] = 1

        for row in range(ROWS):
            for col in range(COLS):
                if obstacleGrid[row][col] == 1:
                    paths[col] = 0
                    continue
                
                if col - 1 >= 0:
                    paths[col] += paths[col - 1]

            print(paths)
        return paths[-1] 
