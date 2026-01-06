# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_sum = -float("inf")
        ans = 0
        level = 1
        queue = deque([root])

        while queue:
            sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if sum > max_sum:
                max_sum = sum
                ans = level
            
            level += 1
        
        return ans

        