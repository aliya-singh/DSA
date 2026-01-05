# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorder(self, root):
        if not root:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        self.l.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.l = []
        self.postorder(root)
        return self.l