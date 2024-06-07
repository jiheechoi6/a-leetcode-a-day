class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] > 0:
                    top = mat[i-1][j] if i > 0 else math.inf
                    left = mat[i][j-1] if j > 0 else math.inf
                    mat[i][j] = min(top, left) + 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] > 0:
                    bottom = mat[i+1][j] if i < (m-1) else math.inf
                    right = mat[i][j+1] if j < (n-1) else math.inf
                    mat[i][j] = min(mat[i][j], bottom+1, right+1)
        
        return mat
