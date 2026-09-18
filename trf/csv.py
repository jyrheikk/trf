import csv

from trf.player import Player

def parse_csv(filename: str, skip_header: bool, delimiter = ',', extra_fields = 0) -> list[Player]:
    LAST_NAME = 0 + extra_fields
    FIRST_NAME = 1 + extra_fields
    CLUB = 2 + extra_fields
    RATING = 3 + extra_fields

    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        if skip_header:
            next(reader)
        result = []
        for row in reader:
            result.append(Player(
                row[FIRST_NAME],
                row[LAST_NAME],
                row[RATING] if len(row) > RATING else '',
                row[CLUB] if len(row) > CLUB else '',
            ))
        return result
