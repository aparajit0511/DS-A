class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if root == None:
            return None

        if root.val == val:
            return root

        ptr = root
        parent = None

        while ptr is not None:

            if ptr.val == val:
                return ptr
            if val <= ptr.val:
                parent = ptr
                ptr = ptr.left
            elif val > ptr.val:
                parent = ptr
                ptr = ptr.right

        return None