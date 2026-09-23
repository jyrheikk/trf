from trf.log import fatal
from trf.player import Player
from trf.rating_list_parser import RatingListParser
from trf.search import binary_search

class RatingList:
    def __init__(self, ratings_file: str):
        parser = RatingListParser()
        self.players = parser.parse(ratings_file, header=True)

    def search_all(self, participants: list[Player]) -> list[Player]:
        found = []
        for p in participants:
            found.append(self.search(p))
        return sorted(found, key=lambda p: p.rating, reverse=True)

    def search(self, p: Player) -> Player:
        player = self.search_unique(p) or self.search_unique(p, by_name=True)
        if not player:
            player = p
            player.set_new()
        return player

    def search_unique(self, p: Player, by_name = False) -> Player | None:
        def key(x: Player) -> str:
            return x.search_name if by_name else x.search_name_club
        i = binary_search(self.players, key(p), key=key)
        if i == -1:
            return None
        elif by_name:
            self.verify_unique_name(p, i)
        return self.players[i]

    def verify_unique_name(self, p: Player, i: int) -> None:
        duplicate = self.search_duplicate(p, i - 1) or self.search_duplicate(p, i + 1)
        if duplicate:
            fatal(
                'Duplicates found, add Club in the players list:\n' +
                self.players[i].name_rating +
                '\n' +
                duplicate.name_rating
            )

    def search_duplicate(self, p: Player, i: int) -> Player | None:
        if i > -1 and i < len(self.players) and self.players[i].is_namesake(p):
            return self.players[i]
        return None
