# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : index for index, val in enumerate(inorder)} # O(n) map for fast lookup
        pre_index = [0] # Use list to make pre_idx mutable in nested function

        def helper(left, right):
            if left > right:
                return None # No elements to construct the subtree
            
            # Get current root value and create node
            root_val = preorder[pre_index[0]]
            root = TreeNode(root_val)

            # Move to next preorder index
            pre_index[0] += 1

            # Build left and right subtrees
            mid = inorder_map[root_val]
            root.left = helper(left, mid - 1) # Left subtree
            root.right = helper(mid + 1, right) # Right subtree

            return root
        
        return helper(0, len(inorder) - 1)
        