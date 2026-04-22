class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights:
            return []

        pacific = set()
        atlantic = set()

        rows, columns = len(heights), len(heights[0])

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = dr + r
                nc = dc + c

                if (0 <= nr < rows and 0 <= nc < columns and (nr, nc) 
                not in visited and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        for c in range(columns):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, columns - 1, atlantic)

        return list(pacific & atlantic)
