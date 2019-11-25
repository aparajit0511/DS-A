class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        
        return self.sumleaf(root, True)
    
    def isLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        
        return False
        
    def sumleaf(self, root, isLeft):
        if root is None: 
            return 0
        if self.isLeaf(root):
            if isLeft:
                return root.val
            else:
                return 0
        else:
            return self.sumleaf(root.left, True) + self.sumleaf(root.right, False)



### With understandable code

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        
        return self.sumleaf(root, True)
    
    def isLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        
        return False
        
    def sumleaf(self, root, isLeft):
        if root is None: 
            return 0
        if self.isLeaf(root):
            if isLeft:
                return root.val
            else:
                return 0
        else:
            left = self.sumleaf(root.left, True) 
            right = self.sumleaf(root.right, False)
            
            return left+right

