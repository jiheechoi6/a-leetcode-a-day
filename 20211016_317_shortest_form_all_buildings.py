class Solution:
    dirc = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return -1
        
        dist = copy.deepcopy(grid)
        m = len(grid)
        n = len(grid[0])
        
        walk = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                
                q = [(i, j, 0)]
                dist[i][j] = 0
                mindist = -1
                for nei in q:
                    for direction in self.dirc:
                        nw = (nei[0]+direction[0], nei[1]+direction[1])
                        if nw[0] >=0 and nw[0]<m and nw[1]>=0 and nw[1]<n and grid[nw[0]][nw[1]] == walk:
                            q.append((nw[0], nw[1], nei[2]+1))

                            grid[nw[0]][nw[1]] -= 1
                            dist[nw[0]][nw[1]] += nei[2]+1
                            
                            if mindist == -1:   
                                mindist = dist[nw[0]][nw[1]]
                            else:   
                                mindist = min(mindist, dist[nw[0]][nw[1]])
                    
                walk -=1
        
        return mindist
                
                    
        
