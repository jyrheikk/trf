DEFAULT_RATING = '1525'

class Player:
    def __init__(self, first_name: str, last_name: str, rating = DEFAULT_RATING, club = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating
        self.club = club
        club_info = f'({club.lower()})' if club else ''
        self.search_name = f'{last_name.lower()}, {first_name.lower()} {club_info}'
