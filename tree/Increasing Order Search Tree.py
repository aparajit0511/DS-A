# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        inorder = []
        root1 = None

        inorder = self.inorder(root,inorder)

        root1 = self.createTree(root1,inorder)

        return root1


    def createTree(self,root,inorder):
        temp = None
        for i in inorder:

            if root is None:
                root = TreeNode(i)
                temp = root
            else:
                root.right = TreeNode(i)
                root = root.right

        return temp

    def inorder(self,root,inorder):
        if root is None:
            return inorder

        self.inorder(root.left,inorder)
        
        inorder.append(root.val)

        self.inorder(root.right,inorder)
        
        return inorder
        

