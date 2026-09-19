from trf.log import fatal
from trf.search import binary_search

DEFAULT_RATING = '1525'

NO_CLUB = '-'
UNOFFICIAL_CLUB = '/'
INACTIVE_SUFFIX = ' #'

class Player:
    def __init__(self, first_name: str, last_name: str, rating = DEFAULT_RATING, club = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating
        self.club = Player.parse_club(club)
        self.has_license = False
        self.is_new = False
        self.__set_helper_fields()

    def __set_helper_fields(self) -> None:
        optional_first_name = f', {self.first_name}' if self.first_name else ''
        self.name = f'{self.last_name}{optional_first_name}'
        optional_club = f' ({self.club})' if self.club else ''
        self.name_club = f'{self.name}{optional_club}'
        self.name_rating = f'{self.name_club} {self.rating}'
        self.__search_name = self.name.lower()
        self.__search_name_club = self.name_club.lower()

    def set_license(self) -> None:
        self.has_license = True

    def set_new(self) -> None:
        self.is_new = True

    def __eq__(self, other) -> bool:
        return self.__search_name == other.__search_name and self.rating == other.rating

    def search(self, players: list[Player], only_name = False) -> Player | None:
        i = binary_search(
            players,
            self.__search_name if only_name else self.__search_name_club,
            key=lambda x: x.__search_name if only_name else x.__search_name_club
        )
        if i == -1:
            return None
        elif only_name:
            self.verify_unique_name(players, i)
        return players[i]

    def verify_unique_name(self, players: list[Player], i: int) -> None:
        duplicate = self.search_duplicate(players, i - 1) or self.search_duplicate(players, i + 1)
        if duplicate:
            fatal(
                'Duplicates found, add Club in the players list:\n' +
                players[i].name_rating +
                '\n' +
                duplicate.name_rating
            )

    def search_duplicate(self, players: list[Player], i: int) -> Player | None:
        if i > -1 and i < len(players) and self.__search_name == players[i].__search_name:
            return players[i]
        return None

    @staticmethod
    def parse_club(club: str) -> str:
        if club == NO_CLUB or UNOFFICIAL_CLUB in club:
            return ''
        elif club.endswith(INACTIVE_SUFFIX):
            return club[:-len(INACTIVE_SUFFIX)]
        else:
            return club
