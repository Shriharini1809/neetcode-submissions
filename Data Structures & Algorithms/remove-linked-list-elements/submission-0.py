# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        prev = cur
        while cur:
            if cur.val != val:
                prev = cur
            else:
                if head == cur:
                    head = head.next
                prev.next = cur.next
            cur = cur.next
        return head
        