class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        rstart, rend, cstart, cend = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while rstart <= rend and cstart <= cend:
            for i in range(rstart, cend + 1):
                res.append(matrix[rstart][i])
            rstart += 1

            for i in range(rstart, rend+1):
                res.append(matrix[i][cend])
            cend -= 1

            if rstart <= rend:
                for i in range(cend, cstart-1, -1):
                    res.append(matrix[rend][i])
                rend -= 1
            
            if cstart <= cend:
                for i in range(rend, rstart - 1, -1):
                    res.append(matrix[i][cstart])
                cstart += 1
        
        return res
