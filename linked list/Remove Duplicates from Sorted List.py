# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        temp = head
        hash_table = []

        head1 = temp1 = temp
        hash_table.append(temp.val)
        temp = temp.next

        while temp is not None:
            if temp.val is not in hash_table:
                temp1 = temp1.next
                temp1 = temp
                hash_table.append(temp.val)

            temp = temp.next

        return head1