class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build graph and in-degree array
        graph = defaultdict(list)        # course → list of dependent courses
        in_degree = [0] * numCourses     # in_degree[i] = # prerequisites of course i

        for dest, src in prerequisites:
            graph[src].append(dest)      # src → dest (you must take src before dest)
            in_degree[dest] += 1         # dest has one more prerequisite

        # Step 2: Initialize queue with courses having 0 prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Step 3: Process courses in topological order
        completed_courses = 0

        while queue:
            course = queue.popleft()
            completed_courses += 1      # Count this course as completed

            # Reduce in-degree of dependent courses
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, it’s ready to be taken
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses are completed
        return completed_courses == numCourses
        