class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cubes = [set() for _ in range(9)]
        
        for i, j in product(range(9), repeat=2):
            val = board[i][j]
            if val == '.':
                continue
            else:
                cube_idx = (i//3)*3+j//3
                if val in rows[i] or val in cols[j] or val in cubes[cube_idx]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                cubes[cube_idx].add(val)
                
        return True
