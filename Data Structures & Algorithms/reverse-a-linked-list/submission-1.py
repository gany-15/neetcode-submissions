# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid, tail = head.next, head.next.next
        head.next = None

        while mid is not None:
            mid.next = head
            head = mid
            mid = tail
            tail = tail.next if tail and tail.next else None
        
        return head
