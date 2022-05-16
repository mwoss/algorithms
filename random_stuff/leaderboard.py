# support for updating the points, after that return current place in leaderboard
#
# Example:
# givePoint("Bob") -> 1   // 1. Bob (1)
# givePoint("Bob") -> 1   // 1. Bob  (2)
# givePoint("Alice") -> 2 // 1. Bob  (2) 2. Alice (1)
# givePoint("Alice") -> 1 // 1. Bob  (2) 1. Alice (2)
# givePoint("Carol") -> 3 // 1. Bob  (2) 1. Alice (2) 3. Carol (1)

from dataclasses import dataclass


@dataclass
class Position:
    behind: int
    player_count: int


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
        self.points_to_player = {}
        self.ranking = {}  # unordered ranking, each position say how many players are behind in ranking

    def give_point(self, player_name: str) -> int:
        """
        Maybe combination of balanced tree + hashmap to store ranking info?
        Or maybe store leaderboard as adjacency matrix, use additional map for quick access to nodes,
        and second map for node to place mapping

        Or we can store information about points to list of player mapping and update only neighbours.
        We can also store information about how many players are higher in ranking that current player too.
        """
        current_points: int = self.points_to_player.get(player_name, 0)

        rank: Position = self.ranking.get(current_points, Position(0, 0))
        next_rank: Position = self.ranking.get(current_points + 1, Position(0, 0))

        new_rank = Position(max(rank.behind + rank.player_count - 1, 0), next_rank.player_count + 1)

        self.points_to_player[player_name] = current_points + 1
        self.ranking[current_points + 1] = new_rank
        self.ranking[current_points] = Position(rank.behind, max(rank.player_count - 1, 0))

        return len(self.points_to_player) - new_rank.behind - new_rank.player_count + 1


if __name__ == '__main__':
    leaderboard = Leaderboard2()
    print(leaderboard.give_point("Bob"))
    print(leaderboard.give_point("Alice"))
    print(leaderboard.give_point("Bob"))
    print(leaderboard.give_point("Bob"))
    print(leaderboard.give_point("Alice"))
    print(leaderboard.give_point("Joyce"))
