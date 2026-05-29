# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        ioSi = inorder.index(root.val)

        ioL, ioR = inorder[:ioSi], inorder[ioSi+1:]
        if len(ioL):
            root.left = self.buildTree(preorder[1:1+len(ioL)], ioL)
        if len(ioR):
            root.right = self.buildTree(preorder[-len(ioR):], ioR)
        return root