# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def len(self, head):
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next

        return count

    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        n = self.len(head)
        m = n//2 + 1
        count = 0
        itr = head

        while itr or itr.next:
            count += 1
            if count == m:
                break
            itr = itr.next

        return itr

        