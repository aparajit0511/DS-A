# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp3 = head3 = None

        temp1,temp2 = l1,l2
        carry = 0

        while temp1 and temp2:

            sum_ = temp1.val + temp2.val + carry
            carry = 0

            if sum_ <= 9:
                head3 = addnode(sum_,head3)
            else:
                sum_1 = sum_ % 10
                head3 = addnode(sum_1,head3)
                carry = sum_ // 10

            temp1 = temp1.next
            temp2 = temp2.next

        # print(temp1.val,carry)
        if temp1 is not None:
            while temp1 is not None:
                sum_ = carry + temp1.val
                carry = 0

                if sum_ > 9:
                    sum_1 = sum_ % 10
                    head3 = addnode(sum_1,head3)
                    carry = sum_ // 10
                else:
                    head3 = addnode(sum_,head3)

                temp1 = temp1.next

        elif temp2 is not None:
            while temp2 is not None:
                sum_ = carry + temp2.val
                carry = 0

                if sum_ > 9:
                    sum_1 = sum_ % 10
                    head3 = addnode(sum_1,head3)
                    carry = sum_ // 10
                else:
                    head3 = addnode(sum_,head3)

                temp2 = temp2.next

        if carry > 0:
            temp3 = head3

            while temp3.next is not None:
                temp3 = temp3.next

            temp = ListNode(carry)
            temp3.next = temp

        return head3

def addnode(sum_,head):

    ptr = ListNode(sum_)

    if head == None:
        head = ptr
    else:
        temp = head

        while temp.next is not None:
            temp = temp.next

        temp.next = ptr

    return head
