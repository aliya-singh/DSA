# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count = 0
        itr = head
        while itr:
            count += 1
            itr = itr.next

        if count == n:
            return head.next
        
        x = count - n - 1
        c = 0
        itr = head
        while c < x:
            c += 1
            itr = itr.next
        
        itr.next = itr.next.next
        return head


