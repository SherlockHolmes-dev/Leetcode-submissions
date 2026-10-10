class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build adjacency list graph: b → a (you must take b before a)
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        # Step 2: visited and recursion stack
        visited = [False] * numCourses
        onPath = [False] * numCourses  # nodes currently in the DFS stack

        def dfs(course):
            # If node is already in current recursion stack → cycle detected
            if onPath[course]:
                return False
            # If already visited and no cycle from here, skip
            if visited[course]:
                return True

            # Mark current node as visited and add to path
            visited[course] = True
            onPath[course] = True

            # Visit all neighbors (courses depending on this course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False  # cycle found

            # Done with this node; remove from current path
            onPath[course] = False
            return True

        # Step 3: DFS from each course
        for course in range(numCourses):
            if not dfs(course):
                return False  # Cycle detected

        return True  # No cycle found
        