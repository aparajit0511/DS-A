class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        while head and head.val == val:
            head = head.next
    
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:      
                cur = cur.next
    
        return head


