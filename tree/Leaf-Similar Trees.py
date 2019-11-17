# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        result1 = []
        result2 = []

        result1 = self.check_leaf(root1,result1)
        result2 = self.check_leaf(root2,result2)
        print(result1,result2)

        if len(result1) != len(result2):
            return False

        for i in range(len(result1)):
            if result1[i] != result2[i]:
                return False

        return True

    def check_leaf(self,root,result):

        if root is None:
            return result
        else:
            result = self.check_leaf(root.left,result)

            if root.left is None and root.right is None:
                result.append(root.val)

            result = self.check_leaf(root.right,result)
            
        return result



