# support for updating the points, after that return current place in leaderboard

class Leaderboard:
    def __init__(self):
        self.points_to_player = {}  # "bob": 2, "alice": 2

    def give_point(self, player_name: str) -> int:
        points = self.points_to_player.get(player_name, 0)

        self.points_to_player[player_name] = points + 1
        sorted_points = sorted(self.points_to_player.values(), reverse=True)

        return sorted_points.index(points + 1) + 1


if __name__ == '__main__':
    l = Leaderboard()
    print(l.give_point("Bob"))
    print(l.give_point("Alice"))
    print(l.give_point("Bob"))
    print(l.give_point("Alice"))
    print(l.give_point("Joyce"))
