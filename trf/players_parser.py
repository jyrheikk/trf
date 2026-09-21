import csv

from trf.player import Player

FREE_GAMES = 10

class PlayersParser:
    def __init__(self):
        self.LAST_NAME = 0
        self.FIRST_NAME = 1
        self.CLUB = 2
        self.RATING = 3
        self.delim = ','

    def parse(self, filename: str, header: bool) -> list[Player]:
        with open(filename, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=self.delim)
            if header:
                next(reader)
            result = []
            for row in reader:
                p = Player(
                    last_name=self.get_value(self.LAST_NAME, row),
                    first_name=self.get_value(self.FIRST_NAME, row),
                    club=self.get_value(self.CLUB, row),
                    rating=self.get_value(self.RATING, row)
                )
                self.parse_optional_fields(row, p)
                result.append(p)
            return result

    def parse_optional_fields(self, row: str, player: Player) -> None:
        pass

    @staticmethod
    def get_value(i: int, row: str) -> str:
        return row[i] if len(row) > i else ''
