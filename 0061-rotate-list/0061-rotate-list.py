# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if head is None or head.next is None or k == 0:
            return head
        
        n = 0
        itr = head
        while itr:
            n += 1
            itr = itr.next
        
        x = k % n
        b = n-x
        if x == 0:
            return head
        c = 0
        itr = head
        while c<b-1:
            c += 1
            itr = itr.next
        
        new_head = itr.next
        itr.next = None
        h = new_head
        while h.next:
            h = h.next    
        h.next = head
        return new_head


