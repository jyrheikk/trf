from trf.player import Player
from trf.rated_players import RatedPlayers

TEST_RATINGS = 'test/test-ratings.csv'

def test_search_all() -> None:
    rated = RatedPlayers(TEST_RATINGS)
    participants = [
        Player('jyrki', 'heikkinen', '', 'lauttssk'),
        Player('Somebody', 'Not Rated')
    ]
    result = rated.search_all(participants)
    assert len(result) == 2
    p1 = result[0]
    assert p1.first_name == 'Jyrki' and p1.last_name == 'Heikkinen' and p1.rating == '2064'
    p2 = result[1]
    assert p2.first_name == 'Somebody' and p2.last_name == 'Not Rated' and p2.rating == '1525'
