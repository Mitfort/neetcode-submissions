class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N,M = len(grid), len(grid[0])
        n_islands = 0;  

        def dfs(i,j):
            if i < 0 or j < 0 or i >= N or j >= M or grid[i][j] == "0":
                return 

            grid[i][j] = "0"

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    dfs(i,j)
                    n_islands += 1 

        print(grid)

        return n_islands