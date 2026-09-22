import pytest

from trf.club import parse_club

@pytest.mark.parametrize('club', ['LauttSSK', 'LauttSSK #'])
def test_parse_club(club: str) -> None:
    assert parse_club(club) == 'LauttSSK'

@pytest.mark.parametrize('club', ['KJ/Lauttasaari', '-', ''])
def test_parse_club_to_empty(club: str) -> None:
    assert parse_club('KJ/Lauttasaari') == ''
