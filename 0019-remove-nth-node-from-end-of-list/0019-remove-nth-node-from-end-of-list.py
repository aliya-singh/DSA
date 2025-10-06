# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def length(self, head):
        count = 0
        if head is None:
            return count
        
        itr = head
        while itr:
            count += 1
            itr = itr.next
        
        return count

    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        m = self.length(head)
        x = m-n-1

        if m == n:
            return head.next
        
        itr = head


        count = 0
        while count < x:
            itr = itr.next
            count += 1

        itr.next = itr.next.next
        
        return head


            



