# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = {}
        itr = head
        i = -1
        while itr and 2 not in d.values():
            if itr not in d:
                d[itr] = 1
            else:
                d[itr] += 1
            itr = itr.next
        
        for i in d:
            if d[i] == 2:
                return i
