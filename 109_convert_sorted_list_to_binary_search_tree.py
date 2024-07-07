# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        if not head.next: return TreeNode(head.val)

        prevmid, mid = self.getMidNode(head)
        midNode = TreeNode(mid.val)
        midNode.right = self.sortedListToBST(mid.next)
        prevmid.next = None
        midNode.left = self.sortedListToBST(head)

        return midNode
    
    def getMidNode(self, head: ListNode) -> Tuple[TreeNode]:
        slo = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slo
            slo = slo.next
            fast = fast.next.next
        
        return prev, slo
        
