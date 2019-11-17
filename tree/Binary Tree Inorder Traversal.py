# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
                
        if root is None:
            return None
        
        inorder = []
        
        inorder = self.isbinarysearch(root,inorder)
            
        return inorder

    def isbinarysearch(self,root,inorder):

        if root is None:
            return inorder

        self.isbinarysearch(root.left,inorder)
        
        inorder.append(root.val)

        self.isbinarysearch(root.right,inorder)
        
        return inorder
        