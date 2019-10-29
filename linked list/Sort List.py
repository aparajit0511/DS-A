# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        
        temp = head

        linked_list = []

        while temp is not None:
            linked_list.append(temp.val)
            temp = temp.next

        linked_list.sort()

        temp =  ptr = head = None

        head = ListNode(linked_list[0])

        ptr = head

        for i in range(1,len(linked_list)):
            temp = ListNode(linked_list[i])
            ptr.next = temp
            ptr = ptr.next

        return head