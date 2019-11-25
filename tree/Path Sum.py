# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        result = 0
        
        return self.pathsum(root,sum,result)

    def pathsum(self,root,sum,result):

        if root is None:
            return False
        else:
            result = result + root.val
            leftFound = self.pathsum(root.left,sum,result)

            rightFound = self.pathsum(root.right,sum,result)
            if root.left is None and root.right is None:
                print(result)
                if result != sum:
                    return False
                else:
                    return True
        return leftFound or rightFound