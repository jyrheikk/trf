from trf.player import Player
from trf.trf import create_players

def test_create_players() -> None:
    players = [
        Player('Tomi', 'Nybäck', '2614'),
        Player('Toivo', 'Keinänen', '2521')
    ]
    expected = [
        '001    1      Nybäck, Tomi                      2614',
        '001    2      Keinänen, Toivo                   2521'
    ]
    trf = create_players(players)
    assert trf == expected
