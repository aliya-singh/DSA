# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        mod = 10**9 + 7
        self.max_pro = 0

        def total_sum(root):
            if not root:
                return 0
            
            return root.val + total_sum(root.left) + total_sum(root.right)
        
        total = total_sum(root)

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            sub_sum = root.val + left + right

            self.max_pro = max(self.max_pro, sub_sum * (total - sub_sum))
            return sub_sum

        dfs(root)
        return self.max_pro % mod
            
