"""
README: TODO

n: numbers of rooms(doctors) in hospital
patients: list of patients (tuple with entrance time and vaccination time)

"""
from typing import List, Tuple


def find_most_occupied_doc(rooms: int, patients: List[Tuple[int, int]]) -> int:
    room_occupation = [(0, 0) for _ in range(rooms)]  # visits, occupied_until
    most_occupied_room = (0, 0)  # idx, occupation

    # if we assume patients list is not sorted by entrance times we need sort it before calculating rooms' occupation
    patients.sort(key=lambda p: p[0])

    for entrance, vaccination_time in patients:
        free_room_idx = find_first_free_room(room_occupation, entrance)
        current_visits = room_occupation[free_room_idx][0]

        room_occupation[free_room_idx] = (current_visits + 1, entrance + vaccination_time)

        if most_occupied_room[1] < current_visits + 1:
            most_occupied_room = (free_room_idx, current_visits + 1)

    return most_occupied_room[0]


def find_first_free_room(room_occupation, entrance):
    for room_idx, (visits, occupied_until) in enumerate(room_occupation):
        if occupied_until < entrance:
            return room_idx
    raise RuntimeError("Couldn't find any free room in hospital")


if __name__ == '__main__':
    patients = [
        (15, 10),
        (20, 7),
        (26, 10),
        (28, 1),
        (30, 1)
    ]
    print(find_most_occupied_doc(5, patients))
