# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head
        

        slow = None
        current = head
        count_size = 1

        while current is not None:

            if count_size % 2 == 0:
                slow.next = current.next

                if count_size == 2:
                    head = current
                else:
                    slow_copy.next = current

                current.next = slow
                current = slow
                slow_copy = slow

            else:
                slow = current

            count_size+=1
            current = current.next

        return head
