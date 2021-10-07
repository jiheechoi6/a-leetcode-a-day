"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.dfs(grid, 0, 0, len(grid))
        
    def dfs(self, grid, row_start: int, col_start: int, length: int):
        zeros = 0
        ones = 0
        is_break = False
        for i in range(int(row_start), int(row_start+length)):
            for j in range(int(col_start), int(col_start+length)):
                if grid[i][j] == 1:
                    ones += 1
                else:
                    zeros += 1
                
                if ones>0 and zeros>0:
                    is_break = True
                    break
            if is_break:
                break
                
        if ones==0 or zeros==0:
            val = bool(ones)
            return Node(val, True, None, None, None, None)
        else:
            length = length/2
            topleft = self.dfs(grid, row_start, col_start, int(length))
            topright = self.dfs(grid, row_start, col_start+length, int(length))
            bottomleft = self.dfs(grid, row_start+length, col_start, int(length))
            bottomright = self.dfs(grid, row_start+length, col_start+length, int(length))
            
            return Node(True, False, topleft, topright, bottomleft, bottomright)
