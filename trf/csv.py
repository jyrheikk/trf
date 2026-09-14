import csv

from trf.player import Player

def parse_rated_players(filename: str) -> list[Player]:
    number_of_extra_fields = 3
    return __parse_csv(filename, ';', number_of_extra_fields)

def parse_participants(filename: str) -> list[Player]:
    return __parse_csv(filename)

def __parse_csv(filename: str, delimiter = ',', extra_fields = 0) -> list[Player]:
    LAST_NAME = 0 + extra_fields
    FIRST_NAME = 1 + extra_fields
    CLUB = 2 + extra_fields
    RATING = 3 + extra_fields

    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        next(reader) # skip header
        result = []
        for row in reader:
            result.append(Player(
                row[FIRST_NAME],
                row[LAST_NAME],
                row[RATING] if len(row) > RATING else '',
                row[CLUB],
            ))
        return result
