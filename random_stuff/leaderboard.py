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
        self.players_behind = {}  # indicates how many ppl are behind certain ranking

    def give_point(self, player_name: str) -> int:
        """
        Maybe combination of balanced tree + hashmap to store ranking info?
        Or maybe store leaderboard as adjacency matrix, use additional map for quick access to nodes,
        and second map for node to place mapping

        Or we can store information about points to list of player mapping and update only neighbours.
        We can also store information about how many players are higher in ranking that current player too.
        """
        current_points = self.points_to_player.get(player_name, 0)
        behind = self.players_behind.get(current_points + 1, 0)

        self.points_to_player[player_name] = current_points + 1
        self.players_behind[current_points + 1] = behind + 1

        return len(self.playe)


if __name__ == '__main__':
    l = Leaderboard()
    print(l.give_point("Bob"))
    print(l.give_point("Alice"))
    print(l.give_point("Bob"))
    print(l.give_point("Alice"))
    print(l.give_point("Joyce"))
