# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        inorder = []
        sum = 0

        self.inorder(root,inorder)

        for i in range(len(inorder)):

            if inorder[i] >= L and inorder[i] <= R:
                sum += inorder[i]

        return sum


    def inorder(self,root,inorder):

        if root is None:
            return inorder

        else:

            self.inorder(root.left,inorder)

            inorder.append(root.val)

            self.inorder(root.right,inorder)

        return inorder
