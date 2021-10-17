class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return 0
        
        dirc = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        
        m = len(grid)
        n = len(grid[0])
        q = []
        freshnum = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshnum+= 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        minutes = 0
        while len(q) != 0 and freshnum != 0:
            minutes += 1
            new_rottens = []
            for rotten in q:
                for d in dirc:
                    new_row = rotten[0] + d[0]
                    new_col = rotten[1] + d[1]
                    if new_row>=0 and new_row<m and new_col>=0 and new_col<n and grid[new_row][new_col] == 1:
                        freshnum -=1
                        grid[new_row][new_col] = 2
                        new_rottens.append((new_row, new_col))
                        
            q = new_rottens
            
        if freshnum != 0:
            return -1
            
        return minutes
                    
                    
                
