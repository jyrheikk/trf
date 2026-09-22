import urllib.request

from trf.log import fatal
from trf.player import Player
from trf.rating_list_parser import RatingListParser
from trf.search import binary_search
from trf.trf import create_directory

class RatingList:
    def __init__(self, ratings_file: str):
        parser = RatingListParser()
        self.players = parser.parse(ratings_file, header=True)

    def search_all(self, participants: list[Player]) -> list[Player]:
        found = []
        for p in participants:
            found.append(self.search(p))
        return sorted(found, key=lambda p: p.rating, reverse=True)

    def search(self, participant: Player) -> Player:
        player = self.search_unique(participant)
        if not player:
            player = self.search_unique(participant, only_name=True)
        if not player:
            player = Player(
                participant.first_name,
                participant.last_name,
                club=participant.club,
                rating=participant.rating,
            )
            player.set_new()
        return player

    def search_unique(self, p: Player, only_name = False) -> Player | None:
        i = binary_search(
            self.players,
            p.search_name if only_name else p.search_name_club,
            key=lambda x: x.search_name if only_name else x.search_name_club
        )
        if i == -1:
            return None
        elif only_name:
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
        if i > -1 and i < len(self.players) and p.search_name == self.players[i].search_name:
            return self.players[i]
        return None

    @staticmethod
    def download(ratings_file: str) -> None:
        url = 'https://www.shakki.net/selo/selolista.csv'
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('latin-1')
        create_directory(ratings_file)
        with open(ratings_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
