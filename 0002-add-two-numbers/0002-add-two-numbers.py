# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lenl1 = 0
        lenl2 = 0
        itr = l1
        while itr:
            lenl1 += 1
            itr = itr.next
        
        itr = l2
        while itr:
            lenl2 += 1
            itr = itr.next

        if lenl1 > lenl2:
            itr1 = l1
            itr2 = l2
            sum = 0
            rem = 0
            while itr1:
                if itr2:
                    sum = itr1.val + itr2.val + rem
                    itr2 = itr2.next
                else:
                    sum = itr1.val + rem
                if sum<10:
                    itr1.val = sum
                    rem = 0
                else:
                    itr1.val = sum%10
                    rem = sum//10
                itrr = itr1
                itr1 = itr1.next
            else:
                if rem != 0:
                    node = ListNode(rem)
                    itrr.next = node
        


            return l1
        
        else:
            itr1 = l1
            itr2 = l2
            sum = 0
            rem = 0
            while itr2:
                if itr1:
                    sum = itr1.val + itr2.val + rem
                    itr1 = itr1.next
                else:
                    sum = itr2.val + rem
                if sum<10:
                    itr2.val = sum
                    rem = 0
                else:
                    itr2.val = sum%10
                    rem = sum//10
                itrr = itr2
                itr2 = itr2.next
            else:
                if rem != 0:
                    node = ListNode(rem)
                    itrr.next = node
        


            return l2


                
                    


            

    
        


        