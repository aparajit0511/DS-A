# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        from collections import deque
        
        queue = deque()
        traversal = []
        
        if not root:
            return traversal
        
        queue.append(root)
        
        while queue:
            level = []
            level_size = len(queue)
            
            for _ in range(level_size):
                item = queue.popleft()
                level.append(item.val)
                
                if item.left:
                    queue.append(item.left)
                
                if item.right:
                    queue.append(item.right)
        
            traversal.append(level[-1])
        
        return traversal
        