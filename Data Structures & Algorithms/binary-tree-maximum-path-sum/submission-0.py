# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') # Global variable to track the max path sum

        def dfs(node):
            if not node:
                return 0 # Base case: 0 contribution from null nodes
            
            # Recursively compute max sum on left and right
            left_gain = max(dfs(node.left), 0) # If negative, take 0
            right_gain = max(dfs(node.right), 0)

            # Current path sum including both children + current node
            current_sum = node.val + left_gain + right_gain

            # Update global max if current_sum is greater
            self.max_sum = max(self.max_sum, current_sum)

            # Return the maximum gain path going **upwards** (either left or right)
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum
        