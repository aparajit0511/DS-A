class Solution: 
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        fast = fast.next 
        
        for i in range(n):
            fast = fast.next
        
        while(fast is not None): 
            fast = fast.next 
            slow = slow.next    
        slow.next = slow.next.next
        
        return dummy.next