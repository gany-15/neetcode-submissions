# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)
            currSum = root.val + leftSum + rightSum
            self.maxSum = max(self.maxSum, currSum)
            return max(root.val, root.val + leftSum, root.val+rightSum, 0)
        
        self.maxSum = -10e7
        _ = dfs(root)
        return self.maxSum