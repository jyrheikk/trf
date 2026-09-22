from trf.club import parse_club

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
        self.search_name = self.name.lower()
        self.search_name_club = self.name_club.lower()

    def set_fide_number(self, fide_number: str) -> None:
        self.fide_number = fide_number

    def set_needs_license(self) -> None:
        self.needs_license = True

    def set_new(self) -> None:
        self.is_new = True

    def __eq__(self, other) -> bool:
        return self.search_name == other.search_name and self.rating == other.rating
