class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Approach is to create sets for each row, column and box

        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue

                boxIndex = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in columns[c] or val in boxes[boxIndex]:
                    return False

                rows[r].add(val)
                columns[c].add(val)
                boxes[boxIndex].add(val)

        return True