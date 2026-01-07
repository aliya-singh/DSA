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
        self.max_sum = 0
        mod = 10**9 + 7

        def total(root):
            if not root:
                return 0
            
            return root.val + total(root.left) + total(root.right)
        
        total = total(root)
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            sub_sum = root.val + left + right
            self.max_sum = max(self.max_sum, (total - sub_sum) * sub_sum)

            return sub_sum
        
        dfs(root) 
        return self.max_sum % mod
