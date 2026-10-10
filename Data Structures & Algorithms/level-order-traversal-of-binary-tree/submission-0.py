# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        # Final result to hold the list of levels
        res = []

        # Initialize queue with root node
        queue = deque([root])

        # While there are nodes to process
        while queue:
            level_size = len(queue) # Number of nodes at current level
            level = [] # List to hold current level's values

            # Process all nodes at the current level
            for i in range(level_size):
                node = queue.popleft() # Pop node from front of the queue
                level.append(node.val) # Add its value to the level list

                # Add child nodes of current node to queue (for next level)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            # After processing the level, append the level list to result                
            res.append(level)

        # Return the level order traversal result           
        return res
        