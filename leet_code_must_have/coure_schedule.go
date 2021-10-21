package main

import (
	"container/list"
	"fmt"
)

func canFinish(numCourses int, prerequisites [][]int) bool {
	graph := make([][]int, numCourses)
	degrees := make([]int, numCourses)

	for _, prerequisite := range prerequisites {
		u, v := prerequisite[0], prerequisite[1]
		graph[v] = append(graph[v], u)
		degrees[u] += 1
	}

	queue := list.New()
	for courseId, degree := range degrees {
		if degree == 0 {
			queue.PushBack(courseId)
		}
	}

	for queue.Len() > 0 {
		curr := queue.Front().Value.(int)
		queue.Remove(queue.Front())
		numCourses -= 1

		for _, n := range graph[curr] {
			degrees[n] -= 1
			if degrees[n] == 0 {
				queue.PushBack(n)
			}
		}
	}

	return numCourses == 0
}

func main() {
	fmt.Println(canFinish(2, [][]int{{1, 0}}))
	fmt.Println(canFinish(3, [][]int{{1, 0}, {0, 1}}))
	fmt.Println(canFinish(3, [][]int{{0, 2}, {1, 2}, {2, 0}}))
}
