from trf.club import parse_club
from trf.log import fatal
from trf.search import binary_search

DEFAULT_RATING = '1525'

class Player:
    def __init__(self, first_name: str, last_name: str, rating = '', club = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating or DEFAULT_RATING
        self.club = parse_club(club)
        self.fide_number = ''
        self.needs_license = False
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

    def set_fide_number(self, fide_number: str) -> None:
        self.fide_number = fide_number

    def set_needs_license(self) -> None:
        self.needs_license = True

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
