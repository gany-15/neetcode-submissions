"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        oldToNew = {}
        h = head
        while h:
            node = Node(h.val)
            oldToNew[h] = node
            h = h.next
        
        h = head
        while h:
            oldToNew[h].next = oldToNew[h.next] if h.next else None
            oldToNew[h].random = oldToNew[h.random] if h.random else None
            h = h.next
        
        return oldToNew[head]
