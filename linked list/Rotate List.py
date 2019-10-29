class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        count = 0
        slow = fast = curr = head
        if not head or not head.next or k == 0:
            return head
        
        while curr:
            count += 1
            curr = curr.next
        k %= count 
        
        if k == 0:
            return head 
        
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        temp = slow.next
        fast.next = head
        slow.next = None
        
        return temp