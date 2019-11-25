# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        inorder = []
        
        inorder = self.inorder(root,inorder)
        
        if len(set(inorder)) == 1:
            return -1
        
        if len(set(inorder)) == 2:
            return max(inorder)
        
        inorder.sort()
        
        for i in range(len(inorder)-1):
            if inorder[i] != inorder[i+1]:
                break
        
        return inorder[i+1]
        
        
    def inorder(self,root,inorder):
        
        if root is None:
            return inorder
        else:
            inorder = self.inorder(root.left,inorder)
            inorder.append(root.val)
            inorder = self.inorder(root.right,inorder)
            
        return inorder
        