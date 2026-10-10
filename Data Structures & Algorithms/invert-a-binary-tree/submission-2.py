# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty subtree
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            # Swap left and right
            temp = node.left
            node.left = node.right
            node.right = temp

            # Push children to stack
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
        
        return root       