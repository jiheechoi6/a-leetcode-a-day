# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cur_max = 0
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.cur_max = -math.inf
        if root is None:
            return 0
        
        one_max = self.findMax(root)
        return max(self.cur_max, one_max)
        
    def findMax(self, root):
        if root is None:
            return 0
        
        left_max = self.findMax(root.left)
        right_max = self.findMax(root.right)        
        
        if left_max > 0 and right_max >0:
            self.cur_max = max(self.cur_max, root.val+left_max+right_max)
        
        onemax = max(left_max+root.val, right_max+root.val, root.val)
        self.cur_max = max(self.cur_max, onemax)
    
        return onemax
        
