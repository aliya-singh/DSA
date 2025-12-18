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
        itr = head
        n = 0
        while itr:
            n += 1
            itr = itr.next
        
        r = k % n
        if r == 0:
            return head
        
        a = n-r
        c = 0
        itr = head
        while c<a-1:
            itr = itr.next
            c += 1
        
        new_head = itr.next
        itr.next = None
        h = new_head
        while h.next:
            h = h.next
        
        h.next = head
        return new_head

        

