# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA is None or headB is None:
            return None
        
        itr1, itr2 = headA, headB
        while itr1 != itr2:
            itr1 = itr1.next if itr1 else headB
            itr2 = itr2.next if itr2 else headA
        
        return itr2
   