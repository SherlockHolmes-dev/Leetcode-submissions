# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative BFS Solution
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are null → same
        if not p and not q:
            return True

        # One is null and the other isn't → not same
        if not p or not q:
            return False

        # Values do not match → not same
        if p.val != q.val:
            return False

        # Recursively compare left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        