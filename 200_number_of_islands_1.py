class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(row, col):
            grid[row][col] = "0"

            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newrow, newcol = i + row, j + col
                if 0<= (newrow) < m and 0 <= (newcol) < n and grid[newrow][newcol] == '1':
                    dfs(newrow, newcol)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count
