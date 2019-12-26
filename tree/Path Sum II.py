# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        result = []
        sum_array = []
        result_sum = 0

        result = self.inorder(root,result,sum_array,result_sum,sum)

        return result

    def inorder(self,root,result,sum_array,result_sum,sum):

        if root is None:
            return result
        else:
            result_sum = result_sum + root.val
            sum_array.append(root.val)

            result = self.inorder(root.left,result,sum_array,result_sum,sum)
            result = self.inorder(root.right,result,sum_array,result_sum,sum)

            if root.left is None and root.right is None:
                if result_sum == sum:
                    result.append(sum_array[:])
            sum_array.pop()

        return result
