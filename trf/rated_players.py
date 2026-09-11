import urllib.request

from trf.args import RATINGS_FILE
from trf.csv import parse_rated_players
from trf.player import Player

class RatedPlayers:
    @staticmethod
    def download():
        url = 'https://www.shakki.net/selo/selolista.csv'

        with urllib.request.urlopen(url) as response:
            content = response.read().decode('latin-1')

        with open(RATINGS_FILE, 'w', encoding='utf-8') as outfile:
            outfile.write(content)

    @staticmethod
    def parse() -> list[Player]:
        return parse_rated_players(RATINGS_FILE)

    @staticmethod
    def sort_by_rating(players: list[Player]) -> list[Player]:
        return sorted(players, key=lambda p: p.rating, reverse=True)
