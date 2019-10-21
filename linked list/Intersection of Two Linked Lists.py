# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        

        ptrA = headA

        while ptrA is not None:
            ptrB = headB

            while ptrB is not None:
                if ptrB == ptrA:
                    return ptrB

                ptrB = ptrB.next

            ptrA = ptrA.next

        return None



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        hash_table = []

        ptrA = headA

        while ptrA is not None:
            hash_table.append(ptrA)
            ptrA = ptrA.next

        ptrB = headB

        while ptrB is not None:
            if ptrB in hash_table:
                return ptrB
            ptrB = ptrB.next

        return None




class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        hash_table = {}

        # ptrA = headA

        while headA is not None:
            hash_table[headA] = headA.next
            headA = headA.next

        # ptrB = headB

        while headB is not None:
            if headB in hash_table:
                return headB
            headB = headB.next

        return None