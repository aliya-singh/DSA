# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        itr1 = l1
        itr2 = l2
        dummy = ListNode(-1)
        prev = dummy
        b = 0
        while itr1 and itr2:
            x = itr1.val + itr2.val + b
            if x < 10:
                a = ListNode(x)
                prev.next = a
                # print(a)
                b = 0
                prev = prev.next
            else:
                c = x%10
                a = ListNode(c)
                prev.next = a
                # print(c)
                b = x//10
                prev = prev.next
    
            itr1 = itr1.next
            itr2 = itr2.next
        
        while itr1:
            x = itr1.val + b
            if x<10:
                a = ListNode(x)
                prev.next = a
                prev = prev.next
                b = 0
            else:
                c = x%10
                a = ListNode(c)
                prev.next = a
                prev = prev.next
                b = x//10
            itr1 = itr1.next
        
        while itr2:
            x = itr2.val + b
            if x<10:
                a = ListNode(x)
                prev.next = a
                prev = prev.next
                b = 0
            else:
                c = x%10
                a = ListNode(c)
                prev.next = a
                prev = prev.next
                b = x//10
            itr2 = itr2.next 

        if b:
            a = ListNode(b)
            prev.next = a    
    


        return dummy.next
                

            