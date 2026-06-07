# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        one, two = dummy, head
        
        i = 1
        while two and two.next:
            if i >= n:
                one = one.next
            two = two.next
            i += 1
        
        one.next = one.next.next
        return dummy.next
