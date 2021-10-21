package main


func canFinish(numCourses int, prerequisites [][]int) bool {
	prerequisiteMapping := make(map[int]int)

	for _, prerequisite := range prerequisites {
		a, b := prerequisite[0], prerequisite[1]
		prerequisiteMapping[b] = a
	}

	for _, prerequisite := range prerequisites {
		slow, fast := prerequisite[0], prerequisite[0]
		//fast, exists := prerequisiteMapping[prerequisite[1]]
		//if !exists {
		//	continue
		//}

		for ; fast, exists := prerequisiteMapping[fast] ;
	}
}