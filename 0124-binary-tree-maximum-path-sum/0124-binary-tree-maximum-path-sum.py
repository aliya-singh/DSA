# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = 0

        def dfs(root):
            if not root:
                return 0
            
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            curr_sum = root.val + left + right
            self.max_sum = max(self.max_sum, curr_sum)

            return root.val + max(left, right)
        
        dfs(root)
        return self.max_sum
