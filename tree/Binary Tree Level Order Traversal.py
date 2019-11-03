# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        from collections import deque

        queue = deque([])
        result = []
        
        ptr = root
        result.append(root.val)
        queue.append(ptr)

        while ptr is not None:

            if ptr.left is not None:
                result.append(ptr.left.val)
                queue.append(ptr.left)

            if ptr.right is not None:
                result.append(ptr.right.val)
                queue.append(ptr.right)

            queue.popleft()
            ptr = queue[0]

        return list(result)