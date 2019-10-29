# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if head == None:
            return None

        temp = head
        temp1 = temp2 = head1 = head2 = ptr = None

        while temp is not None:

            if temp.val < x:
                if head1 == None:
                    head1 = ListNode(temp.val)
                    temp1 = head1
                else:
                    ptr = ListNode(temp.val)
                    temp1.next = ptr
                    temp1 = temp1.next

            else:
                if head2 == None:
                    head2 = ListNode(temp.val)
                    temp2 = head2
                else:
                    ptr = ListNode(temp.val)
                    temp2.next = ptr
                    temp2 = temp2.next

            temp = temp.next

        if head1 == None:
            return head2
        elif head2 == None:
            return head1
        else:
            temp1.next = head2

        return head1