# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None

        if root.val == val:
            return root

        if val <= root.val:
            root.left = self.searchBST(root.left,val)
            return root.left
        else:
            root.right = self.searchBST(root.right,val)
            return root.right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if root == None:
            return None

        if root.val == val:
            return root

        ptr = root
        parent = None

        while ptr is not None:

            if ptr.val == val:
                return ptr
            if val <= ptr.val:
                parent = ptr
                ptr = ptr.left
            elif val > ptr.val:
                parent = ptr
                ptr = ptr.right

        return None

