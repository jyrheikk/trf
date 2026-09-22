import pytest
from pytest import CaptureFixture

from trf.player import Player
from trf.rating_list import RatingList

TEST_RATINGS = 'test/data/test-ratings.csv'

rating_list = RatingList(TEST_RATINGS)

def test_search() -> None:
    participants = [
        Player('jyrki', 'heikkinen', '', 'lauttssk'),
        Player('Somebody', 'Not Rated')
    ]
    expected = [
        Player('Jyrki', 'Heikkinen', '2047', 'LauttSSK'),
        Player('Somebody', 'Not Rated', '1525')
    ]
    assert rating_list.search_all(participants) == expected

def test_search_succeeds_with_only_name() -> None:
    participant = Player('erkki', 'aalto', '', 'Wrong Club')
    player = rating_list.search_unique(participant, only_name=True)
    assert player == Player('Erkki', 'Aalto', '1629', 'HämSK')

def test_search_fails_with_incorrect_club() -> None:
    participant = Player('erkki', 'aalto', '', 'club typo')
    assert not rating_list.search_unique(participant)

def test_search_fails_with_duplicate_names(capsys: CaptureFixture[str]) -> None:
    expected = 'Duplicates found'
    participant = Player('jyrki', 'heikkinen')
    with pytest.raises(SystemExit) as exit_msg:
        rating_list.search_unique(participant, only_name=True)
    output = capsys.readouterr()
    assert expected in output.err or expected in output.out or expected in str(exit_msg.value)
