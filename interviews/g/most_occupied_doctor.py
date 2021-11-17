"""
README: TODO

n: numbers of rooms(doctors) in hospital
patients: list of patients (tuple with entrance time and vaccination time)

"""
from dataclasses import dataclass
from typing import List


@dataclass
class Room:
    id: int
    visits: int = 0
    occupied_until: int = 0


@dataclass
class Patient:
    entrance_time: int
    vaccination_time: int


def find_most_occupied_doc(n_rooms: int, patients: List[Patient]) -> int:
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


if __name__ == '__main__':
    patients = [
        Patient(15, 10),
        Patient(20, 7),
        Patient(26, 10),
        Patient(28, 1),
        Patient(30, 1)
    ]
    print(find_most_occupied_doc(5, patients))
