min_v = -4297867186543
max_v = 4297867186543

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.isbinarysearch(root,min_v,max_v)

    def isbinarysearch(self,root,min_v,max_v):

        if root is None:
            return True

        if root.val > min_v and root.val < max_v and self.isbinarysearch(root.left,min_v,root.val) and self.isbinarysearch(root.right,root.val,max_v):
            return True
        else:
            return False


        

### Inorder soolution



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        inorder = []
        
        inorder = self.isbinarysearch(root,root.val,inorder)
        
        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
            
        return True

    def isbinarysearch(self,root,val,inorder):

        if root is None:
            return inorder

        self.isbinarysearch(root.left,val,inorder)
        
        inorder.append(root.val)

        self.isbinarysearch(root.right,val,inorder)
        
        return inorder
        

