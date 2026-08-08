class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))

        distance = 0

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                if row > 0 and grid[row - 1][col] != -1:
                    if grid[row - 1][col] > distance + 1:
                        grid[row - 1][col] = distance + 1
                        q.append((row - 1, col))

                if row < ROWS - 1 and grid[row + 1][col] != -1:
                    if grid[row + 1][col] > distance + 1:
                        grid[row + 1][col] = distance + 1
                        q.append((row + 1, col))

                if col > 0 and grid[row][col - 1] != -1:
                    if grid[row][col - 1] > distance + 1:
                        grid[row][col - 1] = distance + 1
                        q.append((row, col - 1))

                if col < COLS - 1 and grid[row][col + 1] != -1:
                    if grid[row][col + 1] > distance + 1:
                        grid[row][col + 1] = distance + 1
                        q.append((row, col + 1))

            distance += 1