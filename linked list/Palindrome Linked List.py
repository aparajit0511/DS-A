# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []

        temp = head

        while temp is not None:
            res.append(temp)
            temp = temp.next

        left = 0
        right = len(res)-1

        while left < right:
            if res[left] != res[right]:
                return False
            else:
                left+=1
                right-=1

        return True