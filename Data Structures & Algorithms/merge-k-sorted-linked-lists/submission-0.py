# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodeList = []
        for i, li in enumerate(lists):
            if li:
                heapq.heappush(nodeList, (li.val, i, li))
        
        ansList = ListNode()
        ansPointer = ansList
        while nodeList:
            liVal, i, li = heapq.heappop(nodeList)
            ansPointer.next = ListNode(liVal)
            li = li.next
            ansPointer = ansPointer.next

            if li:
                heapq.heappush(nodeList, (li.val, i, li))
        
        return ansList.next
        