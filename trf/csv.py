import csv

from trf.player import Player

def parse_csv(filename: str, skip_header: bool, delimiter = ',', extra_fields = 0) -> list[Player]:
    LAST_NAME = 0 + extra_fields
    FIRST_NAME = 1 + extra_fields
    CLUB = 2 + extra_fields
    RATING = 3 + extra_fields
    LICENSE = 13 + extra_fields

    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        if skip_header:
            next(reader)
        result = []
        for row in reader:
            p = Player(
                first_name=get_value(FIRST_NAME, row),
                last_name=get_value(LAST_NAME, row),
                rating=get_value(RATING, row),
                club=get_value(CLUB, row),
            )
            if get_value(LICENSE, row) == 'L':
                p.set_license()
            result.append(p)
        return result

def get_value(i: int, row: list[str]) -> str:
    return row[i] if len(row) > i else ''
