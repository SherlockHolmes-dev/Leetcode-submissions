# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper to check if two trees are the same
        def isSameTree(s: TreeNode, t: TreeNode) -> bool:
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        # Main logic: try matching at current node or its children
        if not root:
            return False

        if isSameTree(root, subRoot):
            return True

        # Recurse left and right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        