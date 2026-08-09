class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS,COLS = len(board), len(board[0])

        visited = [[False for _ in range(COLS)] for row in range(ROWS)]
        self.found = False

        def backtrack(i,j, letterIdx, currWord):
            if word[letterIdx] != board[i][j] or visited[i][j]:
                return
            
            if currWord == word or self.found:
                self.found = True
                return

            visited[i][j] = True
            print(currWord)

            if i > 0:
                backtrack(i-1,j, letterIdx + 1, currWord + board[i-1][j])
            
            if i < ROWS - 1:
                backtrack(i+1,j, letterIdx + 1, currWord + board[i+1][j])

            if j > 0: 
                backtrack(i,j-1, letterIdx + 1, currWord + board[i][j-1])
            
            if j < COLS - 1:
                backtrack(i,j+1, letterIdx + 1, currWord + board[i][j+1])

            visited[i][j] = False
            
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] != word[0]:
                    continue
                
                backtrack(i,j,0,word[0])

        return self.found
        
    



            