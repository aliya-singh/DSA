# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        itr = head
        d = {}
        while itr and 2 not in d.values():
            if itr.next not in d:
                d[itr.next] = 1
            else:
                d[itr.next] += 1
            itr = itr.next
        
        if 2 in d.values():
            return True
        else:
            return False