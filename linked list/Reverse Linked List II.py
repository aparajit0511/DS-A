# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        current = head

        if n-m < 1:
            return head

        mark_m , mark_n = 1,1
        flag_m , flag_n = 0,0

        ptr_mark_m, ptr_mark_b4_m, ptr_mark_n, ptr_mark_af4_n = None,None,None,None

        headR, tailR = None,None

        while current is not None:

            if m == 1:
                ptr_mark_m = head
            elif mark_m+1 == m:
                ptr_mark_b4_m = current
                ptr_mark_m = current.next
                flag_m = 1

            if mark_n == n:
                ptr_mark_n = current
                ptr_mark_af4_n = current.next
                flag_n = 1

            if flag_m == 1 and flag_n == 1:
                break

            mark_m+=1
            mark_n+=1

            current = current.next
        
        ptr_mark_n.next = None

        headR = reverse(ptr_mark_m)



        if ptr_mark_m == head:
            ptr_mark_m = headR
            head = addnode(headR,ptr_mark_af4_n)
        else:
            # ptr_mark_b4_m.next = headR
            ptr_mark_b4_m.next = addnode(headR,ptr_mark_af4_n)
        
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

def addnode(head,tail):

    temp = head

    while temp.next is not None:
        temp = temp.next

    temp.next = tail

    return head