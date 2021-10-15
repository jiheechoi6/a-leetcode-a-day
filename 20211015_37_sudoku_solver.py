class Solution:
    row_used = None
    col_used = None
    cube_used = None
    empty = None
    board = None
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.row_used = collections.defaultdict(set)
        self.col_used = collections.defaultdict(set)
        self.cube_used = collections.defaultdict(set)
        self.empty = []
        for i, j in product(range(9), repeat=2):
            val = board[i][j]
            if val == '.':
                self.empty.append((i, j))
            else:
                self.row_used[i].add(val)
                self.col_used[j].add(val)
                self.cube_used[(i//3)*3+j//3].add(val)
        self.board = board
        self.backtrack(0) 
        board = self.board
        return board
    
    def backtrack(self, idx):
        if idx == len(self.empty):  # all empty spots filled
            return True
        
        row, col = self.empty[idx]
        for cand in range(1, 10):
            cand = str(cand)
            if cand in self.row_used[row] or cand in self.col_used[col] or cand in self.cube_used[(row//3)*3+col//3]:
                continue
            else:
                self.board[row][col] = cand
                self.row_used[row].add(cand)
                self.col_used[col].add(cand)
                self.cube_used[(row//3)*3+col//3].add(cand)
                final = self.backtrack(idx+1)
                if final:
                    return True
                self.board[row][col] = '.'
                self.row_used[row].remove(cand)
                self.col_used[col].remove(cand)
                self.cube_used[(row//3)*3+col//3].remove(cand)
                
        
        
