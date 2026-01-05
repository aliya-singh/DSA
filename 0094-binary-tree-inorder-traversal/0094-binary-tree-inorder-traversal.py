# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.l.append(root.val)
        self.inorder(root.right)

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.l = []
        self.inorder(root)

        return self.l