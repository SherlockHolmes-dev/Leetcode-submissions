# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # If both p and q are smaller, move left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are larger, move right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                # This is the split point — LCA found
                return root
        