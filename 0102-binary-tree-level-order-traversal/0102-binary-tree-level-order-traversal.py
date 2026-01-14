# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        l = []
        if not root:
            return l
        
        queue = deque([root])

        while queue:
            ll = []
            for _ in range(len(queue)):
                node = queue.popleft()
                ll.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            l.append(ll)
        
        return l

