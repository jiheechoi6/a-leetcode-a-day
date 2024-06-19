# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        map = {}
        return self.dfs(root, map)

    def dfs(self, root, map):
        if not root: return None
        if root in map: return map[root]

        newNode = NodeCopy(root.val)
        map[root] = newNode

        newNode.left = self.dfs(root.left, map)
        newNode.right = self.dfs(root.right, map)
        newNode.random = self.dfs(root.random, map)

        return newNode
        
