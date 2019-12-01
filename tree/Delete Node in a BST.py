# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if root is None:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            # Deleted node found
            # Case1: No Child

            if root.left is None and root.right is None:
                root = None

            # Case2: One Child
            elif root.left is None:
                temp = root.right
                root = None
                root = temp
            elif root.right is None:
                temp = root.left
                root = None
                root = temp

            # Case3: 2 children
            else:
                temp = self.FindMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)

        return root

    def FindMin(self,root):
        temp = root

        while temp.left is not None:
            temp = temp.left

        return temp


