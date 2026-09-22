import urllib.request

from trf.player import Player
from trf.rating_list_parser import RatingListParser
from trf.trf import create_directory

class RatingList:
    def __init__(self, ratings_file: str):
        parser = RatingListParser()
        self.players = parser.parse(ratings_file, header=True)

    def search(self, participants: list[Player]) -> list[Player]:
        found = []
        for participant in participants:
            player = participant.search(self.players)
            if not player:
                player = participant.search(self.players, only_name=True)
            if not player:
                player = Player(
                    participant.first_name,
                    participant.last_name,
                    club=participant.club,
                    rating=participant.rating,
                )
                player.set_new()
            found.append(player)
        return sorted(found, key=lambda p: p.rating, reverse=True)

    @staticmethod
    def download(ratings_file: str) -> None:
        url = 'https://www.shakki.net/selo/selolista.csv'
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('latin-1')
        create_directory(ratings_file)
        with open(ratings_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
