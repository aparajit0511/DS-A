# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        from collections import deque

        queue = deque()
        traversal = []

        queue.append(root)

        while queue is not None:

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
                traversal.append(sum(level)/len(level))

        return traversal