def height(root):
    '''
    :param root: root of the given tree.
    :return: Integer, height of the given binary tree
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
    }
    '''
    # code here
    
    if root is None:
        return 0
    else:
        l_height = 0
        r_height = 0
        if root.left is not None:
            l_height = height(root.left)
        
        if root.right is not None:
            r_height = height(root.right)
            
    max_height = max(l_height,r_height)
    
    return max_height+1