# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        inorder = []

        inorder = self.inorder(root,inorder)

        while len(inorder) > 0:
            item = inorder.pop()

            if k - item in inorder:
                return True

        return False

    def inorder(self,root,inorder):

        if root is None:
            return inorder
        else:
            inorder = self.inorder(root.left,inorder)
            inorder.append(root.val)
            inorder = self.inorder(root.right,inorder)

        return inorder