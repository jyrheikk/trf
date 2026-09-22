import urllib.request

from trf.player import Player
from trf.players_parser import PlayersParser
from trf.trf import create_directory

FREE_GAMES = 10

class RatingListParser(PlayersParser):
    def __init__(self):
        self.FIDE_NUMBER = 1
        self.LAST_NAME = 3
        self.FIRST_NAME = 4
        self.CLUB = 5
        self.RATING = 6
        self.RATED_GAMES = 7
        self.LICENSE = 16
        self.delim = ';'

    def parse_optional_fields(self, row: str, player: Player) -> None:
        games = self.get_value(self.RATED_GAMES, row)
        if self.get_value(self.LICENSE, row) != 'L' and games and int(games) > FREE_GAMES:
            player.set_needs_license()
        fide_number = self.get_value(self.FIDE_NUMBER, row)
        if fide_number:
            player.set_fide_number(fide_number)

    @staticmethod
    def download(ratings_file: str) -> None:
        url = 'https://www.shakki.net/selo/selolista.csv'
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('latin-1')
        create_directory(ratings_file)
        with open(ratings_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
