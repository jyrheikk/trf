from trf.search import binary_search

DEFAULT_RATING = '1525'

class Player:
    def __init__(self, first_name: str, last_name: str, rating = DEFAULT_RATING, club = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating
        self.club = club
        club_info = f'({club.lower()})' if club else ''
        self.search_name = f'{last_name.lower()}, {first_name.lower()} {club_info}'
        self.is_new = False

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.search_name == other.search_name

    def set_new(self) -> None:
        self.is_new = True

    def search(self, players: list[Player]) -> Player:
        i = binary_search(
            players,
            self.search_name,
            key=lambda x: x.search_name
        )
        return players[i] if i > -1 else None
