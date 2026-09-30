import csv
import io

from trf.player import Player

class PlayersParser:
    def __init__(self):
        self.LAST_NAME = 0
        self.FIRST_NAME = 1
        self.CLUB = 2
        self.RATING = 3
        self.delim = ','

    def parse_file(self, filename: str, header: bool) -> list[Player]:
        with open(filename, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=self.delim)
            if header:
                next(reader)
            return self.parse(reader)

    def parse_players(self, players: list[str]) -> list[Player]:
        csv_data = '\n'.join(players)
        f = io.StringIO(csv_data.strip())
        reader = csv.reader(f)
        return self.parse(reader)

    def parse(self, players: list[str]) -> list[Player]:
        result = []
        for d in players:
            data = [field.strip() for field in d]
            p = Player(
                last_name=self.get_value(self.LAST_NAME, data),
                first_name=self.get_value(self.FIRST_NAME, data),
                club=self.get_value(self.CLUB, data),
                rating=self.get_value(self.RATING, data)
            )
            self.parse_optional_fields(data, p)
            result.append(p)
        return result

    def parse_optional_fields(self, data: str, player: Player) -> None:
        pass

    @staticmethod
    def get_value(i: int, data: str) -> str:
        return data[i] if len(data) > i else ''
