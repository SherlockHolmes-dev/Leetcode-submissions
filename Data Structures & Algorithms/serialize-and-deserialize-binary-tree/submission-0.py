# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("null")  # Mark None nodes
                return
            res.append(str(node.val))  # Add node value
            dfs(node.left)   # Recurse on left
            dfs(node.right)  # Recurse on right

        dfs(root)
        return ",".join(res)  # Convert list to comma-separated string

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")  # Tokenize the string
        self.idx = 0  # Pointer to current node in vals list

        def dfs():
            if vals[self.idx] == "null":
                self.idx += 1
                return None  # No node here
            
            # Create current node
            node = TreeNode(int(vals[self.idx]))
            self.idx += 1

            # Recurse for left and right
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
