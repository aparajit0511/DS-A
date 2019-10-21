# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        counter1 ,counter2 = l1,l2
        head = ListNode(None)
        l3 = ListNode(None)
        head.next = l3
        
        while counter1 and counter2:
            if(counter1.val < counter2.val):
                l3.next = counter1
                counter1 = counter1.next
                l3 = l3.next
            else:
                l3.next = counter2
                counter2 = counter2.next
                l3 = l3.next
        l3.next = counter1 or counter2
        return head.next.next