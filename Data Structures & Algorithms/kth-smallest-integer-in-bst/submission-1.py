# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        count = 0
        kth = None

        while curr:
            if not curr.left:
                count += 1
                if count == k:
                    kth = curr.val
                curr = curr.right
            else:
                pred = curr.left
                # Find rightmost node in left subtree
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr  # Create thread
                    curr = curr.left
                else:
                    pred.right = None  # Remove thread
                    count += 1
                    if count == k:
                        kth = curr.val
                    curr = curr.right

        return kth
        
        