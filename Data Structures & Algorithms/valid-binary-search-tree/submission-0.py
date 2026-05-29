# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, float('-inf'), float('inf')))

        while q:
            node, l, r = q.popleft()
            if node.val <= l or node.val >= r:
                return False
            if node.left:
                if node.val <= node.left.val:
                    return False
                q.append((node.left, l, node.val))
            if node.right:
                if node.val >= node.right.val:
                    return False
                q.append((node.right, node.val, r))
        return True
            
        