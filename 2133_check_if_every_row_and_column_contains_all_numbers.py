class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in range(n):
            rowset = set()
            colset = set()
            for col in range(n):
                if matrix[row][col] in rowset: return False
                else: rowset.add(matrix[row][col])

                if matrix[col][row] in colset: return False
                else: colset.add(matrix[col][row])
        
        return True
