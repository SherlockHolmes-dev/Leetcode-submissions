# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None

        def dfs(node):
            nonlocal count, ans
            
            if not node:
                return
            
            dfs(node.left)

            # Visit current node
            count += 1
            if count == k:
                ans = node.val
            
            dfs(node.right)
        
        dfs(root)
        return ans
        