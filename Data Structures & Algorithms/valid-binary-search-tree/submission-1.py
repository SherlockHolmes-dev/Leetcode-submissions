# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        
        # Queue stores tuples of (node, min_val, max_val)
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, min_val, max_val = queue.popleft()

            # If node violates the min/max constraint, it's not a BST
            if not min_val < node.val < max_val:
                return False
            
            # Add left child with updated max bound
            if node.left:
                queue.append((node.left, min_val, node.val))
            
            # Add right child with updated min bound
            if node.right:
                queue.append((node.right, node.val, max_val))
        
        return True
        