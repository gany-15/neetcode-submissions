# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        tmp = slow.next
        slow.next = None
        slow = tmp
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        hd, tl = head, prev
        while prev:
            print(prev.val)
            prev = prev.next
        while head:
            print(head.val)
            head = head.next
        while tl:
            hdn, tln = hd.next, tl.next
            hd.next = tl
            hd = hdn
            tl.next = hd
            tl = tln
