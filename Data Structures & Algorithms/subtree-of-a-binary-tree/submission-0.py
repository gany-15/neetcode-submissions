# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.tree_string(subRoot) in self.tree_string(root)
    
    def tree_string(self, tree: Optional[TreeNode]) -> str:
        if not tree:
            return '#'
        return f'${tree.val},{self.tree_string(tree.left)},{self.tree_string(tree.right)}'
        