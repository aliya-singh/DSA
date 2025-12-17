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
        itr1 = headA
        itr2 = headB
        len1 = 0
        len2 = 0


        while itr1 or itr2:
            if itr1:
                len1 += 1
                itr1 = itr1.next
            
            if itr2:
                len2 += 1
                itr2 = itr2.next

        diff = abs(len1-len2)

        it1 = headA
        it2 = headB
        count = 0
        if len1 > len2:
            while count < diff:
                count += 1
                it1 = it1.next
        else:
            while count < diff:
                count += 1
                it2 = it2.next
        
        while it1 or it2:
            if it1 == it2:
                return it1
            it1 = it1.next
            it2 = it2.next


