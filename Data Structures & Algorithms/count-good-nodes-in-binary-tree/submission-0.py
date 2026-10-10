# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([(root, root.val)]) # (node, max_so_far)
        count = 0

        while queue:
            node, max_so_far = queue.popleft()

            # If current node is greater or equal to all previous values in the path
            if node.val >= max_so_far:
                count += 1
            
            # Update max for children
            new_max = max(max_so_far, node.val)

            # Add children to the queue with updated max
            if node.left:
                queue.append((node.left, new_max))
            
            if node.right:
                queue.append((node.right, new_max))
            
        return count
        