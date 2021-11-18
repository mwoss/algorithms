"""
README: TODO

n: numbers of rooms(doctors) in hospital
patients: list of patients (tuple with entrance time and vaccination time)

"""
import heapq
from dataclasses import dataclass
from typing import List


@dataclass
class Room:
    id: int
    visits: int = 0
    occupied_until: int = 0

    def __lt__(self, other):
        # used for proper min-heap comparator
        return self.occupied_until < other.occupied_until


@dataclass
class Patient:
    entrance_time: int
    vaccination_time: int


def find_most_occupied_doc(n_rooms: int, patients: List[Patient]) -> int:
    # time complexity: O(np + plgp) ~= O(np)
    # space complexity: O(n)
    if len(patients) == 0:
        return -1  # or throw an exception

    room_occupation = [Room(id=i) for i in range(n_rooms)]  # visits, occupied_until
    most_occupied_room = room_occupation[0]

    # if we assume patients list is not sorted by entrance times we need sort it before calculating rooms' occupation
    patients.sort(key=lambda p: p.entrance_time)

    for patient in patients:
        free_room = find_first_free_room(room_occupation, patient.entrance_time)

        free_room.visits += 1
        free_room.occupied_until = patient.entrance_time + patient.vaccination_time

        if most_occupied_room.visits < free_room.visits:
            most_occupied_room = free_room

    return most_occupied_room.id


def find_first_free_room(rooms: List[Room], entrance_time: int) -> Room:
    for room in rooms:
        if room.occupied_until < entrance_time:
            return room
    raise RuntimeError("Couldn't find any free room in hospital")


def find_most_occupied_doc_optimized(n_rooms: int, patients: List[Patient]) -> int:
    # time complexity: O(p*lgn + p*lgp + n) ~= O(p*lgp)
    # space complexity: O(n)
    del n_rooms  # we know all patients will fit in hospital and we don't need this variable in our heap-based approach

    if len(patients) == 0:
        return -1  # or throw an exception

    # if we assume patients list is not sorted by entrance times we need sort it before calculating rooms' occupation
    patients.sort(key=lambda p: p.entrance_time)

    occupied_rooms = []

    for patient in patients:
        if len(occupied_rooms) == 0 or occupied_rooms[0].occupied_until > patient.entrance_time:
            free_room_id = len(occupied_rooms)
            heapq.heappush(
                occupied_rooms,
                Room(free_room_id, 1, patient.entrance_time + patient.vaccination_time)
            )
        else:
            pfr = occupied_rooms[0]
            heapq.heappushpop(
                occupied_rooms,
                Room(pfr.id, pfr.visits + 1, patient.entrance_time + patient.vaccination_time)
            )

    # finding the most occupied room could be done done in main for-loop, but in sake of simplicity
    # I decided to iterate over all occupied room one more time to find that one room
    most_occupied_room = max(occupied_rooms, key=lambda r: r.visits)
    return most_occupied_room.id


if __name__ == '__main__':
    patients = [
        Patient(15, 10),
        Patient(20, 7),
        Patient(26, 10),
        Patient(28, 1),
        Patient(30, 1)
    ]
    print(find_most_occupied_doc_optimized(5, patients))
