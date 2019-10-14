# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        ptr = new = None
        current = head

        while current is not None:
            ptr = current
            current = current.next
            ptr.next = new
            new = ptr

        head = new

        return head