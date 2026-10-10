# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]  # Use list to make it mutable in nested function

        def dfs(node):
            if not node:
                return 0

            # Compute depth of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Update max diameter at this node
            max_diameter[0] = max(max_diameter[0], left + right)

            # Return depth to parent
            return 1 + max(left, right)

        dfs(root)
        return max_diameter[0]
        