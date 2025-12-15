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
        
        prev = None
        itr = head

        while itr:
            next_ele = itr.next
            itr.next = prev
            prev = itr
            itr = next_ele

        return prev