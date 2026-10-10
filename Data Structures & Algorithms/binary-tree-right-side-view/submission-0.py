# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, depth):
            if not node:
                return
            
            # If this is the first time we're visiting this level, add the node's value
            if depth == len(ans):
                ans.append(node.val)

            # Traverse right subtree first to ensure rightmost node is visited first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        # Start DFS from root at depth 0
        dfs(root, 0)
        return ans
        