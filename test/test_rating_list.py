from trf.player import Player
from trf.rating_list import RatingList

TEST_RATINGS = 'test/data/test-ratings.csv'

def test_search() -> None:
    rating_list = RatingList(TEST_RATINGS)
    participants = [
        Player('jyrki', 'heikkinen', '', 'lauttssk'),
        Player('Somebody', 'Not Rated')
    ]
    expected = [
        Player('Jyrki', 'Heikkinen', '2047', 'LauttSSK'),
        Player('Somebody', 'Not Rated', '1525')
    ]
    assert rating_list.search_all(participants) == expected
