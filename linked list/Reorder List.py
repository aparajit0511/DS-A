# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head

        temp = head
        count_size = 0

        while temp is not None:
            count_size+=1
            temp = temp.next

        temp = head
        head1 = None
        break_point = 0

        while temp is not None:
            break_point+=1

            if count_size % 2 == 0 and break_point == count_size // 2:
                break
            elif count_size % 2 == 1 and break_point == (count_size // 2)+1:
                break

            temp = temp.next


        head1 = temp.next
        temp.next = None

        head1 = reverse(head1)

        temp1 = head
        ptr , ptr1 = None,None

        while temp1 and head1:
            ptr = head1
            head1 = head1.next
            ptr1 = temp1.next
            temp1.next = ptr
            ptr.next = ptr1
            temp1 = temp1.next.next

        return head



def reverse(head):

        ptr = new = None
        current = head

        while current is not None:
            ptr = current
            current = current.next
            ptr.next = new
            new = ptr

        head = new

        return head


