# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        itr = head
        n = 0
        while itr:
            n += 1
            itr = itr.next
        x = n//2
        c = 0
        itr = head
        while c < x:
            c += 1
            itr= itr.next
        
        return itr