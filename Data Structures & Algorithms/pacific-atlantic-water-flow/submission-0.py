class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        # 2 Arrays telling if element is reaching ocean
        Atlantic = [[False] * COLS for _ in range(ROWS)] 
        Pacific = [[False] * COLS for _ in range(ROWS)]

        # SPACE: O(2 * ROWS * COLS)
        # TIME: O(2 * n) , n = all cells 

        # DFS 
        def dfs(i,j,ocean,prevHeight):
            # Edge cases 
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return 
            
            curr = heights[i][j]

            # We search for water going uphill :D 
            if ocean[i][j] or curr < prevHeight:
                return

            ocean[i][j] = True

            # Follow along
            dfs(i+1,j,ocean,curr) # BOTTOM
            dfs(i-1,j,ocean,curr) # TOP
            dfs(i,j-1,ocean,curr) # LEFT
            dfs(i,j+1,ocean,curr) # RIGHT

        # LEFT Pacific and RIGHT Atlantic
        for row in range(ROWS):
            dfs(row,0,Pacific,heights[row][0])
            dfs(row,COLS-1,Atlantic,heights[row][COLS-1])

        # TOP Pacific and BOTTOM Atlantic
        for col in range(COLS):
            dfs(0,col,Pacific,heights[0][col])
            dfs(ROWS-1,col,Atlantic,heights[ROWS-1][col])

        # Return the list of cells which reaches both oceans
        res = []
        
        for i in range(ROWS):
            for j in range(COLS):
                if Atlantic[i][j] and Pacific[i][j]:
                    res.append([i,j])

        return res