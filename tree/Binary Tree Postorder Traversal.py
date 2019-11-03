# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        self.recursion(root,result)
        
        return result
    
    def recursion(self,root,result):
        
        if root == None:
            return 
        else:
            self.recursion(root.left,result)
            self.recursion(root.right,result)
            
            result.append(root.val)