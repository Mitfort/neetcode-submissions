class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N,M = len(board), len(board[0])
        self.found:bool = False

        visited:List[List[bool]] = [[False] * M for _ in range(N)]

        def backtrack(i,j,idx):
            if board[i][j] != word[idx] or self.found or visited[i][j]: return
 
            visited[i][j] = True

            if idx == len(word) - 1:
                self.found = True
                return 

            if i >= 1:
                backtrack(i-1,j,idx+1) # TOP

            if i < N - 1:
                backtrack(i+1,j,idx+1) # BOT
            
            if j >= 1:
                backtrack(i,j-1,idx+1) # LEFT
            
            if j < M - 1:
                backtrack(i,j+1,idx+1) # RIGHT

            visited[i][j] = False

        for i in range(N):
            for j in range(M):
                if not visited[i][j] and board[i][j] == word[0]:
                    backtrack(i,j,0)

        return self.found


                    