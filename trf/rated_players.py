import urllib.request
from pathlib import Path

from trf.csv import parse_csv
from trf.player import Player
from trf.trf import create_directory

class RatedPlayers:
    def __init__(self, ratings_file: str):
        self.players = parse_csv(
            ratings_file,
            header=True,
            delim=';',
            leading_fields=3,
            rating=True
        )

    def search_all(self, participants: list[Player]) -> list[Player]:
        found = []
        for participant in participants:
            player = participant.search(self.players)
            if not player:
                player = participant.search(self.players, only_name=True)
            if not player:
                print(f'Not found: {participant.last_name}')
                player = Player(
                    participant.first_name,
                    participant.last_name,
                    club=participant.club,
                )
                player.set_new()
            found.append(player)
        return sorted(found, key=lambda p: p.rating, reverse=True)

    @staticmethod
    def download(ratings_file: str) -> None:
        url = 'https://www.shakki.net/selo/selolista.csv'
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('latin-1')
        file_path = Path(ratings_file)
        create_directory(file_path.parent)
        with open(ratings_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
