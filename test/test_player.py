import pytest
from pytest import CaptureFixture

from trf.player import Player

RATINGS = [
    Player('Jyrki', 'Heikkinen', '2064', 'LauttSSK'),
    Player('Jyrki', 'Heikkinen', '1602', 'MatSK'),
    Player('Random', 'Surname', '1500', 'X')
]

@pytest.mark.parametrize('club', ['LauttSSK', 'LauttSSK #'])
def test_parse_club(club: str) -> None:
    assert Player.parse_club(club) == 'LauttSSK'

@pytest.mark.parametrize('club', ['KJ/Lauttasaari', '-', ''])
def test_parse_club_to_empty(club: str) -> None:
    assert Player.parse_club('KJ/Lauttasaari') == ''

def test_search_succeeds_with_only_name() -> None:
    participant = Player('random', 'surname', '', 'Wrong Club')
    player = participant.search(RATINGS, only_name=True)
    assert player == Player('Random', 'Surname', '1500', 'X')

def test_search_fails_with_incorrect_club() -> None:
    participant = Player('random', 'surname', '', 'club typo')
    assert not participant.search(RATINGS)

def test_search_fails_with_duplicate_names(capsys: CaptureFixture[str]) -> None:
    expected = 'Duplicates found'
    participant = Player('jyrki', 'heikkinen')
    with pytest.raises(SystemExit) as exit_msg:
        participant.search(RATINGS, only_name=True)
    output = capsys.readouterr()
    assert expected in output.err or expected in output.out or expected in str(exit_msg.value)
