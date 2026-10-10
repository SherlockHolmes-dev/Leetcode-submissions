# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque([root]) # Initialize queue with root node

        while queue:
            level_size = len(queue) # Number of nodes at the current level

            for i in range(level_size):
                node = queue.popleft()

                # If this is the last node in the current level, it's the rightmost one
                if i == level_size - 1:
                    ans.append(node.val)
                
                # Add left and right children to the queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans
        