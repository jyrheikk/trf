import urllib.request

from trf.args import RATINGS_FILE
from trf.csv import parse_rated_players
from trf.player import Player

class RatedPlayers:
    def __init__(self):
        self.players = parse_rated_players(RATINGS_FILE)

    def search_all(self, registrants: list[Player]) -> list[Player]:
        found = []
        for reg in registrants:
            player = reg.search(self.players)
            if player:
                found.append(player)
            else:
                p = Player(reg.first_name, reg.last_name)
                p.set_new()
                found.append(p)
        return sorted(found, key=lambda p: p.rating, reverse=True)

    @staticmethod
    def download() -> None:
        url = 'https://www.shakki.net/selo/selolista.csv'

        with urllib.request.urlopen(url) as response:
            content = response.read().decode('latin-1')

        with open(RATINGS_FILE, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
