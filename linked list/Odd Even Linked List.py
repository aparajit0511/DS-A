# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ptr = head

        headE = temp = ptrE = None

        while ptr is not None and ptr.next is not None:

            temp = ptr.next
            # ptr.next = temp.next
            ptr.next = ptr.next.next
            temp.next = None

            if headE == None:
                headE = temp
            else:
                ptrE = headE

                while ptrE.next != None:
                    ptrE = ptrE.next

                ptrE.next = temp
                
            if ptr.next == None:
                print("hi")
                break

            ptr = ptr.next

        if ptr is None:
            ptr = headE
        else:
            ptr.next = headE

        return head