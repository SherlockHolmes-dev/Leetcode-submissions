"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Dictionary to map original nodes to their cloned copies
        visited = {}

        def dfs(curr):
            # If the node is already cloned, return the clone
            if curr in visited:
                return visited[curr]

            # Clone the current node (create a new node with the same value)
            clone = Node(curr.val)

            # Store the clone in the visited dictionary
            visited[curr] = clone

            # Iterate over the neighbors and clone them recursively
            for neighbor in curr.neighbors:
                # Append cloned neighbor to the clone's neighbors list
                clone.neighbors.append(dfs(neighbor))

            return clone

        # Start DFS from the given node
        return dfs(node)
        