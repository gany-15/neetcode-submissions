# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            leftdepth = dfs(node.left)
            rightdepth = dfs(node.right)
            curr = leftdepth + rightdepth
            self.diameter = max(self.diameter, curr)
            return max(leftdepth, rightdepth) + 1
        
        dfs(root)
        return self.diameter
