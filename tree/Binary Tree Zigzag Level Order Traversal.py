# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result = []

        if root is None:
            return result

        from collections import deque

        queue = deque()

        queue.append(root)
        counter = 0

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                item = queue.popleft()
                level.append(item.val)

                if item.left is not None:
                    queue.append(item.left)
                if item.right is not None:
                    queue.append(item.right)

            counter+=1

            if counter % 2 == 0:
                result.append(reversed(level))
            else:
                result.append(level)

        return result

