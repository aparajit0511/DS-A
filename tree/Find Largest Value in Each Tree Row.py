# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        from collections import deque

        queue = deque()
        max_array = []
        
        if root is None:
            return max_array

        queue.append(root)

        while len(queue) > 0:
            level = []
            level_size = len(queue)

            for _ in range(level_size):

                item = queue.popleft()
                level.append(item.val)

                if item.left is not None:
                    queue.append(item.left)

                if item.right is not None:
                    queue.append(item.right)

            if len(level) > 0:
                max_array.append(max(level))

        return max_array