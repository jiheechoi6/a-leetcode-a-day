# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode(-1)
        vals = []
        
        for sub in lists:
            while sub:
                vals.append(sub)
                sub = sub.next
                
        def cmp(item1):
            return item1.val
        vals.sort(key=cmp)
        
        for val in vals:
            node.next = val
            node = node.next
        return dummy.next
