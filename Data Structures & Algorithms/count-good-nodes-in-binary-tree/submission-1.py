# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # Count this node if it's good (no greater value in the path so far)
            count = 1 if node.val >= max_so_far else 0

            # Update the max value seen so far in the path
            new_max = max(node.val, max_so_far)

            # Recur on left and right children
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count
        
        # Start DFS with the root node and initial max = root's value
        return dfs(root, root.val)
        