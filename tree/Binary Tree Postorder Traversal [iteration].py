# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root == None:
        	return

        stack = []
        result = []

        while True:

        	while root is not None:

        		if root.right is not None:
        			stack.append(root.right)
        		stack.append(root)

        		root = root.left

        	root = stack.pop()

        	if root.right is not None and peek(stack) == root.right:
        		stack.pop()
        		stack.append(root)
        		root = root.right
        	else:
        		result.append(root.val)
        		root = None

        	if len(stack) <= 0:
        		break

        return result

def peek(stack):
    if len(stack) > 0:
    	return stack[-1]
    return None
