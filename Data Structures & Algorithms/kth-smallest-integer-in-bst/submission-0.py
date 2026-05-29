# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        st = []

        node = root

        while True:
            if node:
                st.append(node)
                node = node.left

            elif st:
                node = st.pop()
                s.append(node.val)
                
                if len(s) == k:
                    return s[-1]

                node = node.right