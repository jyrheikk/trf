from trf.search import binary_search

DEFAULT_RATING = '1525'

NO_CLUB = '-'
UNOFFICIAL_CLUB = '/'
INACTIVE_SUFFIX = ' #'

class Player:
    def __init__(self, first_name: str, last_name: str, rating = DEFAULT_RATING, club = '', is_new = False):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating
        self.club = Player.parse_club(club)
        optional_first_name = f', {self.first_name}' if self.first_name else ''
        self.full_name = f'{last_name}{optional_first_name}'
        optional_club = f' ({self.club})' if self.club else ''
        self.full_details = f'{self.full_name}{optional_club}'
        self.search_name = self.full_name.lower()
        self.search_details = self.full_details.lower()
        self.is_new = is_new

    def __eq__(self, other) -> bool:
        return self.search_name == other.search_name and self.rating == other.rating

    def search(self, players: list[Player], only_name = False) -> Player | None:
        i = binary_search(
            players,
            self.search_name if only_name else self.search_details,
            key=lambda x: x.search_name if only_name else x.search_details
        )
        return players[i] if i > -1 else None

    @staticmethod
    def parse_club(club: str) -> str:
        if club == NO_CLUB or UNOFFICIAL_CLUB in club:
            return ''
        elif club.endswith(INACTIVE_SUFFIX):
            return club[:-len(INACTIVE_SUFFIX)]
        else:
            return club
