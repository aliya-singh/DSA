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
        
        if not head or not head.next or k == 0:
            return head

        x = head
        n = 0
        while x:
            n += 1
            x = x.next

        a = k % n

        x = head
        nn = n - a
        count = 0
        if a == 0:
            return head
            
        while count < nn - 1:
            count += 1
            x = x.next
        
        new_head = x.next
        x.next = None

        aa = new_head 
        while aa.next:
            aa = aa.next
        
        aa.next = head


        return new_head