# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def getMaxWidth(root):
    
    if root is None:
        return 0
        
    from collections import deque
    
    queue = deque()
    
    queue.append(root)
    max_width = -1
    
    while queue:
        level_size = len(queue)
        
        max_width = max(level_size,max_width)
        
        for _ in range(level_size):
            item = queue.popleft()
            
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
                
    return max_width
                
             