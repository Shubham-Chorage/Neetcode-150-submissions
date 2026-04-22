from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, columns = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
