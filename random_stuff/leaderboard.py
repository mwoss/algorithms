# support for updating the points, after that return current place in leaderboard

from collections import defaultdict

class PlayerInfo:
    def __init__(self, points, place):
        self.points = points
        self.place = place

class Leaderboard:
    def __init__(self):
        self.player_points = defaultdict(lambda: 0)
        self.buckets = defaultdict(set)


    def give_point(self, player_name: str) -> int:
        prev_points = self.player_points[player_name]

        self.buckets[prev_points].remove(player_name)

        self.player_points[player_name] = prev_points + 1
        self.buckets[prev_points + 1].add(player_name)

        return 0



if __name__ == '__main__':
    print("XDD")
