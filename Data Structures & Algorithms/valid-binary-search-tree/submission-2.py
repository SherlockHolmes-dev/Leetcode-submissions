# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, min_val, max_val):
            if not node:
                return True # An empty node is always valid

            # The current node must be strictly within the (min_val, max_val) range
            if not (min_val < node.val < max_val):
                return False
            
            # Check left subtree with updated max constraint
            left_valid = dfs(node.left, min_val, node.val)

            # Check right subtree with updated min constraint
            right_valid = dfs(node.right, node.val, max_val)

            return left_valid and right_valid
        
        # Initial call with full range
        return dfs(root, float('-inf'), float('inf'))
        