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
        self.grid = grid
        return self.recurse(0, 0, len(grid))
    
    def recurse(self, rowstart, colstart, width):
        onecount = 0
        zerocount = 0
        for row in range(rowstart, rowstart+width):
            for col in range(colstart, colstart+width):
                if self.grid[row][col] == 0:    zerocount += 1
                else:   onecount += 1
                
                if zerocount and onecount:
                    half = width//2
                    topleft = self.recurse(rowstart, colstart, half)
                    topright = self.recurse(rowstart, colstart+half, half)
                    bottomleft = self.recurse(rowstart+half, colstart, half)
                    bottomright = self.recurse(rowstart+half, colstart+half, half)
                    return Node(1, False, topleft, topright, bottomleft, bottomright)
        
        val = 1 if onecount else 0
        return Node(val, True, None, None, None, None)
                
                    
        
