# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = []
        s = ''

        result = self.root_to_leaf(root,result,s)

        return sum(result)

    def root_to_leaf(self,root,result,s):

        if root is None:
            return result

        else:

            s = s + str(root.val)

            result = self.root_to_leaf(root.left,result,s)
            result = self.root_to_leaf(root.right,result,s)

            if root.left is None and root.right is None:
                result.append(int(s))

        return result
