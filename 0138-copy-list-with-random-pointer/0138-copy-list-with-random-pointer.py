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
        
        if head is None:
            return None
        
        temp = head
        d = {}
        while temp:
            d[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            newnode = d[temp]
            newnode.next = d[temp.next] if temp.next else None
            newnode.random = d[temp.random] if temp.random else None
            temp = temp.next
        
        return d[head]
            
        
        