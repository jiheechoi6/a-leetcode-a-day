class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCnt = 0
        que = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: freshCnt +=1
                if grid[r][c] == 2: que.append((r, c))

        res = 0
        while que and freshCnt > 0:
            size = len(que)

            for _ in range(size):
                cont = que.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    newr, newc = cont[0] + dr, cont[1] + dc
                    if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        freshCnt -= 1
                        que.append((newr, newc))
            
            res += 1
        
        if freshCnt != 0: return -1

        return res
        
