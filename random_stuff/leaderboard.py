# support for updating the points, after that return current place in leaderboard

from collections import defaultdict

class PlayerInfo:
    def __init__(self, points, place):
        self.points = points
        self.place = place

class Leaderboard:
    def __init__(self):
        self.points_to_player = {}
        self.points_to_position = {}


    def give_point(self, player_name: str) -> int:
        points = self.points_to_player.get(player_name, 0)
        self.points_to_player[player_name] = points + 1

        return 0



if __name__ == '__main__':
    print("XDD")
