# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  not head or not head.next: return head

        tmp = head.next
        rev = self.reverseList(head.next)
        tmp.next = head
        head.next = None

        return rev
      
