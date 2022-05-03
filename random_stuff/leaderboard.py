# support for updating the points, after that return current place in leaderboard
#
# Example:
# givePoint("Bob") -> 1   // 1. Bob (1)
# givePoint("Bob") -> 1   // 1. Bob  (2)
# givePoint("Alice") -> 2 // 1. Bob  (2) 2. Alice (1)
# givePoint("Alice") -> 1 // 1. Bob  (2) 1. Alice (2)
# givePoint("Carol") -> 3 // 1. Bob  (2) 1. Alice (2) 3. Carol (1)

class Leaderboard:
    def __init__(self):
        self.points_to_player = {}  # "bob": 2, "alice": 2

    def give_point(self, player_name: str) -> int:
        points = self.points_to_player.get(player_name, 0)

        self.points_to_player[player_name] = points + 1
        sorted_points = sorted(self.points_to_player.values(), reverse=True)

        return sorted_points.index(points + 1) + 1


class Leaderboard2:
    def __init__(self):
        self.points_to_player = {}  # "bob": 2, "alice": 2, "joyce: 1 -> 1, 1, 3
        self.snapshots = [{}]

    def give_point(self, player_name: str) -> int:
        points = self.points_to_player.get(player_name, 0)

        prev_snapshot = self.snapshots[-1]


        return 0


if __name__ == '__main__':
    l = Leaderboard()
    print(l.give_point("Bob"))
    print(l.give_point("Alice"))
    print(l.give_point("Bob"))
    print(l.give_point("Alice"))
    print(l.give_point("Joyce"))
