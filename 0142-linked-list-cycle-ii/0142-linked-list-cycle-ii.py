# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        itr = head
        d = {}
        while itr and 2 not in d.values():
            if itr not in d:
                d[itr] = 1
            else:
                d[itr] += 1
            itr = itr.next
        
        if 2 not in d.values():
            return None

        for i in d:
            if d[i] == 2:
                x = i
                break
        
        return x
        # itr = head
        # c = 0
        # while itr:
        #     if itr == x:
        #         break
        #     c += 1
        #     itr = itr.next
        
        # return c

