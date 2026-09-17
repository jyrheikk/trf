import pytest

from trf.player import Player

@pytest.mark.parametrize('club', ['LauttSSK', 'LauttSSK #'])
def test_parse_club(club: str) -> None:
    assert Player.parse_club(club) == 'LauttSSK'

@pytest.mark.parametrize('club', ['KJ/Lauttasaari', '-', ''])
def test_parse_club_to_empty(club: str) -> None:
    assert Player.parse_club('KJ/Lauttasaari') == ''

RATINGS = [
    Player('Jyrki', 'Heikkinen', '2064', 'LauttSSK'),
    Player('Somebody', 'Else', '1500')
]

def test_search_fails_with_incorrect_club() -> None:
    participant = Player('jyrki', 'heikkinen', '', 'club typo')
    assert not participant.search(RATINGS)

def test_search_succeeds_with_only_name() -> None:
    participant = Player('jyrki', 'heikkinen', '', 'club typo')
    player = participant.search(RATINGS, only_name = True)
    assert player == Player('Jyrki', 'Heikkinen', '2064', 'LauttSSK')
