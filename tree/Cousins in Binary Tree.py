# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque
        
        queue = deque()
        
        if not root:
            return False
        
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
                    
                if item.left is not None and item.right is not None:
                    if item.left.val == x and item.right.val == y or item.left.val == y and item.right.val == x:
                        return False
                if x in level and y in level:
                    return True
        
        
        return False
        