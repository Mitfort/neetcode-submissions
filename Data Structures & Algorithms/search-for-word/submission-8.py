class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        N,M = len(board), len(board[0])
        visited = [[False] * M for _ in range(N)]

        self.res = False

        def backtrack(i,j, w_idx):
            if i >= N or i < 0 or j >= M or j < 0:
                return 

            if visited[i][j] or word[w_idx] != board[i][j]: 
                return 

            if w_idx + 1 == len(word):
                self.res = True 
                return 

            visited[i][j] = True

            backtrack(i+1,j,w_idx + 1)
            backtrack(i-1,j,w_idx + 1)
            backtrack(i,j+1,w_idx + 1)
            backtrack(i,j-1,w_idx + 1)

            visited[i][j] = False


        for i in range(N):
            for j in range(M):
                if not visited[i][j]:
                    backtrack(i,j,0)

        return self.res