# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        inorder_left = []
        inorder_right = []

        if root is None:
            return False
        if root.left is None:
            return False
        if root.right is None:
            return False

        inorder_left = self.inorder(root.left,inorder_left)
        inorder_right = self.inorder(root.right,inorder_right)

        if len(inorder_left) != len(inorder_right):
            return False

        for i in range(len(inorder_right)-1,-1):
            if inorder_left[i] != inorder_right[i]:
                return False

        return True

    def inorder(self,root,inorder):

        if root is None:
            return inorder
        else:

            inorder = self.inorder(root.left,inorder)
            inorder.append(root.val)
            inorder = self.inorder(root.right,inorder)

        return inorder


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True
        if root.left is None:
            return False
        if root.right is None:
            return False

        return self.inorder(root.left,root.right)

    def inorder(self,root1,root2):

        if root1 is None and root2 is None:
            return True
        elif root1 is None and root2 is not None:
            return False
        elif root2 is None and root1 is not None:
            return False
        else:

            if(self.inorder(root1.left,root2.right) is True and root1.val == root2.val):
                return True

            if(self.inorder(root1.right,root2.left) is True and root1.val == root2.val):
                return True

        return False



#### Working solution

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        return self.inorder(root.left,root.right)

    def inorder(self,root1,root2):

        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        else:
            if root1.val != root2.val:
                return False
            
            if(self.inorder(root1.left,root2.right) and self.inorder(root1.right,root2.left)):
                return True

        return False

