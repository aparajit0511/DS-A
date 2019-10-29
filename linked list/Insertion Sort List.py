# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        temp = head
        linked_list = []

        while temp is not None:
            linked_list.append(temp.val)
            temp = temp.next

        for i in range(len(linked_list)):
            for j in range(i):
                if linked_list[i] <= linked_list[j]:
                    linked_list[i] , linked_list[j] = linked_list[j] , linked_list[i]

        head = ListNode(linked_list[0])
        temp = head

        for i in range(1,len(linked_list)):

            ptr = ListNode(linked_list[i])
            temp.next = ptr
            temp = temp.next

        return head
