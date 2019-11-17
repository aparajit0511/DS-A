class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        num = self.height(root)
        
        print(num)

        if num == -1:
            return False

        return True

    def height(self,root):

        if root is None:
            return 0

        else:
            l_height = 0
            r_height = 0

            if root.left is not None:
                l_height = self.height(root.left)

            if root.right is not None:
                r_height = self.height(root.right)
                
        if l_height is -1 or r_height is -1:
            return -1

        if l_height > r_height:
            if l_height - r_height > 1:
                return -1
            return l_height+1
        else:
            if r_height - l_height > 1:
                return -1
            return r_height+1