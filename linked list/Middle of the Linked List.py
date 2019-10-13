# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        temp = head
        
        i = 0
        while temp.next is not None:
            i+=1
            temp = temp.next
        
        temp = head
        count = 0
        if i % 2 == 1:
            
            while count <= i//2:
                temp = temp.next
                count+=1
            
            # return temp.val
        else:
            while count <= (i//2)-1:
                temp = temp.next
                count+=1

        return temp
                
        