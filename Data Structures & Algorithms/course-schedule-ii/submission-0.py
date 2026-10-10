class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build the graph and in-degree array
        graph = defaultdict(list)        # course → list of dependent courses
        in_degree = [0] * numCourses     # in_degree[i] = number of prerequisites for course i

        for dest, src in prerequisites:
            graph[src].append(dest)      # To take dest, you must take src first
            in_degree[dest] += 1         # dest has one more prerequisite

        # Step 2: Initialize queue with all courses having 0 prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []  # Final topological order

        # Step 3: Perform BFS (Kahn's Algorithm)
        while queue:
            course = queue.popleft()
            order.append(course)  # Course can be taken now

            # Reduce in-degree for its neighbors (dependent courses)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: If all courses are in order → return it, else return []
        if len(order) == numCourses:
            return order
        else:
            return []  # Cycle detected, not possible
        