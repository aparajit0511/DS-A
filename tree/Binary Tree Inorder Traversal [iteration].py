# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        

        current = root
        stack = []
        inorder = []

        while True:
            if len(stack) == 0 and current == None:
                break

            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()

            inorder.append(current.val)
            current = current.right
            
            print(inorder)

        return inorder