# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        tree_value = []
        
        tree_value = self.inorder(root,tree_value)
        
        if len(set(tree_value)) == 1:
            return True
        
        return False
    
    def inorder(self,root,tree_value):
        
        if root is None:
            return tree_value
        else:
            
            tree_value = self.inorder(root.left,tree_value)
            
            tree_value.append(root.val)
            
            tree_value = self.inorder(root.right,tree_value)
            
        return tree_value
        
        