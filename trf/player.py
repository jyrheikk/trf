from trf.club import parse_club

DEFAULT_RATING = '1525'

SINGLE_QUOTE = '\u0092'

class Player:
    def __init__(self, first_name: str, last_name: str, rating = '', club = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating or DEFAULT_RATING
        self.club = parse_club(club)
        self.needs_license = False
        self.is_new = False
        self.__set_combined_fields()

    def __set_combined_fields(self) -> None:
        optional_first_name = f', {self.first_name}' if self.first_name else ''
        self.name = self.human_readable(f'{self.last_name}{optional_first_name}')
        optional_club = f' ({self.club})' if self.club else ''
        self.name_club = f'{self.name}{optional_club}'
        self.name_rating = f'{self.name_club} {self.rating}'
        self.__search_name = self.encode_search_name(self.name.lower())
        self.__search_name_club = self.encode_search_name(self.name_club.lower())

    @staticmethod
    def human_readable(name: str) -> str:
        return name.replace(SINGLE_QUOTE, "'")

    @staticmethod
    def encode_search_name(name: str) -> str:
        return name.replace("'", SINGLE_QUOTE)

    def __eq__(self, p: Player) -> bool:
        return self.is_namesake(p) and self.rating == p.rating

    def get_search_key(self, by_name = False) -> str:
        return self.__search_name if by_name else self.__search_name_club

    def is_namesake(self, p: Player) -> bool:
        return self.__search_name == p.__search_name

    def set_needs_license(self) -> None:
        self.needs_license = True

    def set_new(self) -> None:
        self.is_new = True
