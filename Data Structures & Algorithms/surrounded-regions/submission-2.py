class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board:
            return None

        rows, columns = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= columns or board[r][c] != "O":
                return 

            board[r][c] = "S"

            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, columns - 1)

        for c in range(columns):
            dfs(0, c)
            dfs(rows - 1,c)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

        
