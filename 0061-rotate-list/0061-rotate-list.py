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
        if not head:
            return
        n = 0
        l = []
        itr = head
        while itr:
            n += 1
            l.append(itr.val)
            itr = itr.next
        
        a = k % n
        b = n - a
        l = l[b:] + l[:b]

        itr = head
        for i in l:
            itr.val = i
            itr = itr.next

        return head


