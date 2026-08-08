class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.counter = 0

        ROWS,COLS = len(grid), len(grid[0])
        
        self.visited = [[0 for col in range(COLS)] for row in range(ROWS)]

        def searchIsland(i,j):
            if grid[i][j] == '0' or self.visited[i][j]:
                return
                
            self.visited[i][j] = 1

            if i > 0: # CHECK TOP
                searchIsland(i-1,j)

            if i < ROWS - 1: # BOT
                searchIsland(i+1,j)

            if j > 0:
                searchIsland(i,j-1) # LEFT
            
            if j < COLS - 1: # RIGHT
                searchIsland(i,j+1)



        for i in range(ROWS):
            for j in range(COLS):
                if self.visited[i][j]:
                    continue
                
                if grid[i][j] == '1':
                    self.counter += 1
                    searchIsland(i,j)

        return self.counter
