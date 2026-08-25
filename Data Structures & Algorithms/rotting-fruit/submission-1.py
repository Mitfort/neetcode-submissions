class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes:int = 0
        ROWS,COLS = len(grid), len(grid[0])

        visited = [[False] * COLS for _ in range(ROWS)]
        q = deque()

        # Save starting points 
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i-1,j))
                    q.append((i+1,j))
                    q.append((i,j+1))
                    q.append((i,j-1))
    
        while q:
            rotted_this_minute = False

            for idx in range(len(q)):
                i,j = q.popleft()
                
                if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                    continue

                if visited[i][j]:
                    continue

                visited[i][j] = True
                curr = grid[i][j]

                if curr == 1:
                    grid[i][j] = 2
                    rotted_this_minute = True
                    q.append((i-1,j))
                    q.append((i+1,j))
                    q.append((i,j+1))
                    q.append((i,j-1))

            if rotted_this_minute:
                minutes+=1 

        # Search if there is any fresh fruit
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return minutes


                