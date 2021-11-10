"""
Given the list of jobs and information about their dependencies return the order of jobs in which they should be executed.
Jobs cannot be executed if all its dependencies were not yet executed.

Note 1: The could be multiple solutions for given list of jobs
Note 2: Some jobs may depend on each other
Note 3: Jobs (IDs) are numerated from 0 to n (for simplicity)
"""
from collections import deque
from dataclasses import dataclass
from typing import List, Set


@dataclass
class Job:
    job_id: int
    dependencies: Set[int]


def schedule_jobs(jobs: List[Job]):
    degrees = [0] * len(jobs)

    for job in jobs:
        degrees[job.job_id] += len(job.dependencies)

    jobs_count = len(jobs)
    top_order, queue = [], deque([])

    for job_id, degree in enumerate(degrees):
        if degree == 0:
            queue.append(job_id)

    while queue:
        job_node = queue.popleft()
        top_order.append(job_node)

        for job in jobs:
            if job_node in job.dependencies:
                degrees[job.job_id] -= 1
                if degrees[job.job_id] == 0:
                    queue.append(job.job_id)

        jobs_count -= 1

    if jobs_count != 0:
        raise RuntimeError("At least two jobs depend on each other (potential cycle in dependency graph)")

    return top_order


if __name__ == '__main__':
    jobs = [Job(0, {1, 2}), Job(1, {3}), Job(2, {1}), Job(3, {})]
    print(schedule_jobs(jobs))
