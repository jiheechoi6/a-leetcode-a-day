# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depthBalanced(self, root):
        if not root: return 0

        lDepth = self.depthBalanced(root.left)
        if lDepth == -1: return -1
        rDepth = self.depthBalanced(root.right)
        if rDepth == -1: return -1

        return max(lDepth, rDepth) + 1 if abs(lDepth - rDepth) <= 1 else -1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depthBalanced(root) != -1
      
