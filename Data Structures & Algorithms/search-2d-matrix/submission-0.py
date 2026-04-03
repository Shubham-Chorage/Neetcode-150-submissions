class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        start = 0
        end = columns - 1

        while start < rows and end >= 0:
            if matrix[start][end] == target:
                return True
            elif matrix[start][end] < target:
                start += 1
            else:
                end -= 1
                
        return False