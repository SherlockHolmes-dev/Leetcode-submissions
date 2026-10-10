# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: empty subtree
        if not root:
            return 0

        # Recursively compute left and right subtree depths
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return the larger of the two + current node
        return 1 + max(left_depth, right_depth)
        