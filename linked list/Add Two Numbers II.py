# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp1 = temp = temp2 = head =None

        node_list1 = []
        node_list2 = []

        temp1 = l1
        temp2 = l2

        while temp1 is not None:
            node_list1.append(temp1.val)
            temp1 = temp1.next

        while temp2 is not None:
            node_list2.append(temp2.val)
            temp2 = temp2.next

        str_list1 = int(''.join(map(str,(node_list1))))
        str_list2 = int(''.join(map(str,(node_list2))))

        sum_ = (str_list1) + (str_list2)

        for item in str(sum_):
            ptr = ListNode(int(item))

            if head == None:
                head = ptr
            else:
                temp = head
                while temp.next is not None:
                    temp = temp.next

                temp.next = ptr

        return head