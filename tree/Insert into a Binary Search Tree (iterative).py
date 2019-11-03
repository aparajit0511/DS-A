class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        ptr = root
        parent = None

        while ptr is not None:

            if val < ptr.val:
                parent = ptr
                ptr = ptr.left
            else:
                parent = ptr
                ptr = ptr.right

        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

        return root