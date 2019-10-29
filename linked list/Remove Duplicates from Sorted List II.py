# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        temp = head
        slow = None
        hash_table = []

        while temp is not None:

            if temp.next != None and temp.val == temp.next.val:
                hash_table.append(temp.val)

                if temp == head:
                    head = head.next.next
                    temp = head
                else:
                    slow.next = temp.next.next
                    temp = slow.next

            elif temp.val in hash_table:

                if temp == head:
                    head = head.next
                    temp = head

                else:
                    slow.next = temp.next
                    temp = slow.next

            else:
                
                slow = temp
                temp = temp.next

        return head