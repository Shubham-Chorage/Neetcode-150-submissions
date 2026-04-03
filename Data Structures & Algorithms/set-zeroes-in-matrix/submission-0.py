class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        columns = len(matrix[0])
        matrix1 = [row[:] for row in matrix]

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    k = 0
                    while k < rows:
                        matrix1[k][j] = 0
                        k += 1
                    l = 0
                    while l < columns:
                        matrix1[i][l] = 0
                        l += 1
                    
        for i in range(rows):
            for j in range(columns):
                matrix[i][j] = matrix1[i][j]