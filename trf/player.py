import re

DEFAULT_RATING = '1525'

class Player:
    def __init__(self, first_name: str, last_name: str, rating = DEFAULT_RATING, club = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating
        self.club = club

    def equals(self, a: Player) -> bool:
        return equals(self.last_name, a.last_name) and \
            equals(self.first_name, a.first_name) and \
            (equals(self.club, a.club) or not self.club or not a.club)

def equals(a: str, b: str) -> bool:
    return re.match(a, b, re.IGNORECASE)
