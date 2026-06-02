"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        root = None
        seen = {}

        def dfs(curr):
            if curr is None:
                return None
            elif curr.val in seen:
                return seen[curr.val]

            newNode = Node(curr.val)
            seen[curr.val] = newNode
            if curr.neighbors and len(curr.neighbors) > 0:
                for neighbor in curr.neighbors:
                    newNode.neighbors.append(dfs(neighbor))
            
            return newNode
        
        root = dfs(node)
        return root
