# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []

        def in_order_traversal(node):

            if not node:
                return
            
            in_order_traversal(node.left)
            inorder.append(node.val) # Collect value
            in_order_traversal(node.right)
        
        in_order_traversal(root)

        # Check for strictly increasing order
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False
        return True
        