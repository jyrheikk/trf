from trf.player import Player
from trf.rated_players import RatedPlayers

TEST_RATINGS = 'test/data/test-ratings.csv'

def test_search_all() -> None:
    rated = RatedPlayers(TEST_RATINGS)
    participants = [
        Player('Aarre', 'Aalto'),
        Player('Erkki', 'Aalto', 'HämSK'),
        Player('jyrki', 'heikkinen', '', 'lauttssk'),
        Player('Somebody', 'Not Rated')
    ]
    expected = [
        Player('Jyrki', 'Heikkinen', '2064', 'LauttSSK'),
        Player('Erkki', 'Aalto', '1949', 'HämSK'),
        Player('Somebody', 'Not Rated', '1525'),
        Player('Aarre', 'Aalto', '1409'),
    ]
    result = rated.search_all(participants)
