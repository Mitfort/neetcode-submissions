class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        ROWS,COLS = len(heights), len(heights[0])

        # Will tell us if from the specific cell we can reach ocean
        pacific:List[List[int]] = [[False] * COLS for _ in range(ROWS)]
        atlantic:List[List[int]] = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)

            while q: 
                i,j = q.popleft()
                ocean[i][j] = True
                height = heights[i][j] 

                if i > 0 and not ocean[i-1][j] and heights[i-1][j] >= height:
                    q.append((i-1,j))

                if j > 0 and not ocean[i][j-1] and heights[i][j-1] >= height:
                    q.append((i,j-1))

                if i < ROWS - 1 and not ocean[i+1][j] and heights[i+1][j] >= height:
                    q.append((i+1,j))

                if j < COLS - 1 and not ocean[i][j+1] and heights[i][j+1] >= height:
                    q.append((i,j+1))

        pacific_valid = []
        atlantic_valid = []

        for c in range(COLS):
            pacific_valid.append((0,c))
            atlantic_valid.append((ROWS-1,c))

        for r in range(ROWS):
            pacific_valid.append((r,0))
            atlantic_valid.append((r,COLS-1))

        print(pacific_valid)
        print(atlantic_valid)

        bfs(pacific_valid,pacific)
        bfs(atlantic_valid,atlantic)

        res = []

        for i in range(ROWS):
            for j in range(COLS):
                if pacific[i][j] and atlantic[i][j]:
                    res.append((i,j))

        return res



        


        