# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        st = [root]
        s = []

        while st:
            node = st.pop()
            if not node:
                s.append('#')
                continue
            s.append(str(node.val))
            st.append(node.right)
            st.append(node.left)
        
        return ",".join(s)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')
        i = 0

        def construct_tree():
            nonlocal i
            if arr[i] == '#':
                return None
            node = TreeNode(int(arr[i]))
            i += 1
            node.left = construct_tree()
            i += 1
            node.right = construct_tree()
            return node
            
        return construct_tree()
