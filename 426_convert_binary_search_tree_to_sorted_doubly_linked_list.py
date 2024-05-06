"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        head = prev = Node()

        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            nonlocal prev
            prev.right = node
            node.left = prev
            prev = node

            traverse(node.right)

        traverse(root)

        head.right.left = prev
        prev.right = head.right

        return head.right
        
