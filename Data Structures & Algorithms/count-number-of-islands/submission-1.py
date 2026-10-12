class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N,M = len(grid), len(grid[0])
        
        visited:List[List[bool]] = [[False] * M for _ in range(N)]

        count:int = 0 

        def dfs(row,col):       
            if row < 0 or col < 0 or row >= N or col >= M:
                return 

            if visited[row][col] or grid[row][col] == '0': 
                return

            visited[row][col] = True 

            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row,col-1)          

        for i in range(N):
            for j in range(M): 
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i,j)
                    count += 1 
        
        return count