# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        itr = head
        prev = None
        while itr:
            x = itr.next
            itr.next = prev
            prev = itr
            itr = x
        
        return prev
