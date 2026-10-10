class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
    
        parent = [i for i in range(n + 1)]  # parent[i] = parent of node i
        rank = [1] * (n + 1)                # rank[i] = size of the tree for union by rank

        def find(x):
            # Path compression
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # Already connected -> Cycle
            # Union by rank
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
                rank[rootY] += rank[rootX]
            else:
                parent[rootY] = rootX
                rank[rootX] += rank[rootY]
            return True

        # Process each edge
        for u, v in edges:
            if not union(u, v):
                return [u, v]  # This edge creates the cycle
        