import urllib.request

from trf.args import INPUT_DIR, RATINGS_FILE
from trf.csv import parse_csv
from trf.player import Player
from trf.trf import create_directory

class RatedPlayers:
    def __init__(self, ratings = RATINGS_FILE):
        self.players = parse_csv(
            ratings,
            skip_header=True,
            delimiter=';',
            extra_fields=3
        )

    def search_all(self, participants: list[Player]) -> list[Player]:
        found = []
        for participant in participants:
            player = participant.search(self.players) if participant.club else None
            if not player:
                player = Player(participant.first_name, participant.last_name)
                player.set_new()
            found.append(player)
        return sorted(found, key=lambda p: p.rating, reverse=True)

    @staticmethod
    def download() -> None:
        url = 'https://www.shakki.net/selo/selolista.csv'

        with urllib.request.urlopen(url) as response:
            content = response.read().decode('latin-1')

        create_directory(INPUT_DIR)
        with open(RATINGS_FILE, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
