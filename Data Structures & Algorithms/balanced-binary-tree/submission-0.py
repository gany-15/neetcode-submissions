# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedReturnDepth(root)[0]

    def isBalancedReturnDepth(self, node:Optional[TreeNode]) -> tuple(bool, int):
        if not node:
            return (True, 0)
        
        leftBal, leftHeight = self.isBalancedReturnDepth(node.left)
        rightBal, rightHeight = self.isBalancedReturnDepth(node.right)


        return (leftBal and rightBal and -1 <= leftHeight - rightHeight <= 1, max(leftHeight, rightHeight) + 1)
