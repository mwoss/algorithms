from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph: List[List[int]] = [[] for _ in range(num_courses)]
    degress = [0 for _ in range(num_courses)]

    for u, v in prerequisites:
        graph[v].append(u)
        degress[u] += 1

    # add vertices (courses) without any dependencies to the queue
    queue = deque([])
    for course, degree in enumerate(degress):
        if degree == 0:
            queue.append(course)

    while queue:
        current = queue.popleft()

        num_courses -= 1  # we can remove courses for which we satisfied all dependencies

        for neighbour in graph[current]:
            degress[neighbour] -= 1
            if degress[neighbour] == 0:
                queue.append(neighbour)

    return num_courses == 0


if __name__ == '__main__':
    print(can_finish(2, [[0, 1]]))
    print(can_finish(2, [[1, 0], [0, 1]]))
