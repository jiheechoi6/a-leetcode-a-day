# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def depth(node):
            nonlocal diameter
            if not node: return 0

            lDepth = depth(node.left)
            rDepth = depth(node.right)

            diameter = max(diameter, lDepth + rDepth)

            return max(lDepth, rDepth) + 1

        depth(root)

        return diameter
        
