class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.cubes = [set() for _ in range(9)]
        self.emptys = []
        
        for i, j in product(range(9), repeat=2):
            val = board[i][j]
            if val == '.':
                self.emptys.append((i, j))
            self.rows[i].add(val)
            self.cols[j].add(val)
            self.cubes[(i//3)*3+j//3].add(val)
        
        return self.backtrack(0)
    
    def backtrack(self, idx):
        if idx == len(self.emptys):  return True
        
        i, j = self.emptys[idx]
        c_idx = (i//3)*3+ j//3
        for cand in range(1, 10):
            cand = str(cand)
            if cand in self.rows[i] or cand in self.cols[j] or cand in self.cubes[c_idx]:
                continue
            
            self.board[i][j] = cand
            self.rows[i].add(cand)
            self.cols[j].add(cand)
            self.cubes[c_idx].add(cand)
            if self.backtrack(idx+1): return True
            self.board[i][j] = '.'
            self.rows[i].remove(cand)
            self.cols[j].remove(cand)
            self.cubes[c_idx].remove(cand)
        
        return False
                
        
        
