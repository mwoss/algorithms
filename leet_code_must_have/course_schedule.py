"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
from collections import deque
from typing import List, Deque


class Solution:
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's / BFS solution
        graph = self._build_graph(num_courses, prerequisites)
        degrees = self._compute_indegrees(graph)

        for i in range(num_courses):
            j = 0
            while j < num_courses:
                if degrees[j] == 0:
                    break
                j += 1

            if j == num_courses:
                return False

            degrees[j] -= 1

            for vertex in graph[j]:
                degrees[vertex] -= 1

        return True

    def _build_graph(self, num_courses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(num_courses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
        return graph

    def _compute_indegrees(self, graph: List[List[int]]) -> List[int]:
        degrees = [0] * len(graph)
        for adj in graph:
            for vertex in adj:
                degrees[vertex] += 1
        return degrees


class Solution2:
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's algorithm (topological sort) but using queue
        graph: List[List[int]] = [[] for _ in range(num_courses)]
        degrees: List[int] = [0] * num_courses

        # build adjacency list from prerequisites (graph representation) and calculate (in)degree of each vertex
        for u, v in prerequisites:
            graph[v].append(u)
            degrees[u] += 1

        # we can freely add vertices that do not have any dependencies
        queue: Deque[int] = deque([])
        for course, degree in enumerate(degrees):
            if degree == 0:
                queue.append(course)

        # traverse throughout out all vertices adn remove dependencies from neighbour vertices
        while queue:
            curr = queue.popleft()
            num_courses -= 1  # we can exclude course that has 0 dependencies

            for adj_vertex in graph[curr]:
                degrees[adj_vertex] -= 1
                if degrees[adj_vertex] == 0:
                    queue.append(adj_vertex)

        return num_courses == 0


if __name__ == '__main__':
    s = Solution2()
    print(s.can_finish(2, [[1, 0]]))
    print(s.can_finish(3, [[1, 0], [0, 1]]))
    print(s.can_finish(3, [[0, 2], [1, 2], [2, 0]]))
