NO_CLUB = '-'
UNOFFICIAL_CLUB = '/'
INACTIVE_SUFFIX = ' #'

def parse_club(club: str) -> str:
    if club == NO_CLUB or UNOFFICIAL_CLUB in club:
        return ''
    elif club.endswith(INACTIVE_SUFFIX):
        return club[:-len(INACTIVE_SUFFIX)]
    else:
        return club
