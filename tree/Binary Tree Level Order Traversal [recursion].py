# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        
        height = tree_height(root)

        result = []

        for i in range(1,height+1):
            levelOrder_recursion(root,i,result)
            
        print(height,result)
        
        return list(result)
        


def tree_height(root):

    if root == None:
        return 0
    else:
        # d1 , d2 = 0 , 0

        d1 = tree_height(root.left)
        d1+=1
        d2 = tree_height(root.right)
        d2+=1

    if d1 >= d2:
        return d1+1
    else:
        return d2+1


def levelOrder_recursion(root,i,result):

    if root == None:
        return 
    elif i == 1:
        result.append(root.val)
    elif i > 1:
        levelOrder_recursion(root.left,i-1,result)
        levelOrder_recursion(root.right,i-1,result)

    return


### Working soltion

class Solution:
    def levelOrder(self, root):
        if not root: return []
        res = []
        self.dfs(root,0,res)
        return res
    def dfs(self, root, level, res):
        if not root:
            return 
        if len(res) < level +1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left,level + 1, res)
        self.dfs(root.right, level+1, res)