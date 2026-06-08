# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        op = []
        
        q.append(root)

        while q:
            levelOp = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                
                levelOp.append(node.val)
                q.append(node.left)
                q.append(node.right)
            
            if len(levelOp):
                op.append(levelOp)
        
        return op
