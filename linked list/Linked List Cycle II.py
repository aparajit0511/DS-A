class Solution:
	def detectCycle(self, head: ListNode) -> ListNode:
		temp = head
		a = []
		while(temp):
			if temp not in a:
				a.append(temp)
			else:
				return temp
			temp = temp.next
		return None