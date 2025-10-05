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
        
        itr = head
        l = 1
        while itr.next:
            itr = itr.next
            l += 1
        itr.next = head
        
        r = k % l
        k = l - r

        itrr = head
        for _ in range(k-1):
            itrr = itrr.next
        
        new_head = itrr.next
        itrr.next = None

        return new_head

