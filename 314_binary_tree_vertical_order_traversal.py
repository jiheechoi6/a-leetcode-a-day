# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columns = collections.defaultdict(list)

        queue = collections.deque([(root, 0)])

        while queue:
            node, column = queue.popleft()
            columns[column].append(node.val)

            if node.left:
                queue.append((node.left, column-1))
            if node.right:
                queue.append((node.right, column+1))

        return [columns[i] for i in range(min(columns), max(columns)+1)]
      
