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
        
        l1 = []
        itr1 = headA
        while itr1:
            l1.append(itr1)
            itr1 = itr1.next

        l2 = []
        itr2 = headB
        while itr2:
            l2.append(itr2)
            itr2 = itr2.next
        
        l1 = l1[::-1]
        l2 = l2[::-1]

        c = 0
        m = min(len(l1), len(l2))
        while c < m and l1[c] == l2[c]:
            c += 1

        if c == 0:
            return None
        else:
            return l1[c-1]

   