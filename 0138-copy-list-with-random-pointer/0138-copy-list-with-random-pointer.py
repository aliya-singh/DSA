"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        itr = head
        d = {}
        while itr:
            d[itr] = Node(itr.val)
            itr = itr.next
        
        itr = head
        while itr:
            new_head = d[itr]
            new_head.next = d[itr.next] if itr.next else None
            new_head.random = d[itr.random] if itr.random else None
            itr = itr.next
        
        return d[head]