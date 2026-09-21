import csv

from trf.player import Player

FREE_GAMES = 10

def parse_csv(filename: str, header: bool, delim = ',', leading_fields = 0) -> list[Player]:
    LAST_NAME = 0 + leading_fields
    FIRST_NAME = 1 + leading_fields
    CLUB = 2 + leading_fields
    RATING = 3 + leading_fields
    RATED_GAMES = 4 + leading_fields
    LICENSE = 13 + leading_fields
    FIDE_NUMBER = 1 # only in the ratings list

    ratings_list = leading_fields > 0

    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delim)
        if header:
            next(reader)
        result = []
        for row in reader:
            p = Player(
                last_name=get_value(LAST_NAME, row),
                first_name=get_value(FIRST_NAME, row),
                club=get_value(CLUB, row),
                rating=get_value(RATING, row)
            )
            if ratings_list > 0:
                games = get_value(RATED_GAMES, row)
                if get_value(LICENSE, row) != 'L' and games and int(games) > FREE_GAMES:
                    p.set_needs_license()
                fide_number = get_value(FIDE_NUMBER, row)
                if fide_number:
                    p.set_fide_number(fide_number)
            result.append(p)
        return result

def get_value(i: int, row: str) -> str:
    return row[i] if len(row) > i else ''
