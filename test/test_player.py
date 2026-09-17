import pytest

from trf.player import Player

@pytest.mark.parametrize('club', ['LauttSSK', 'LauttSSK #'])
def test_parse_club(club: str) -> None:
    assert Player.parse_club(club) == 'LauttSSK'

@pytest.mark.parametrize('club', ['KJ/Lauttasaari', '-', ''])
def test_parse_club_empty(club: str) -> None:
    assert Player.parse_club('KJ/Lauttasaari') == ''
