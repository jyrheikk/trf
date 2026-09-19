from trf.player import Player
from trf.trf import create_groups

TOURNAMENT_INFO = '''012 Test {GROUP}
022 Helsinki
'''

GROUP_A = '''012 Test A
022 Helsinki

001    1      Nybäck, Tomi                      2614
001    2      Keinänen, Toivo                   2521
'''

GROUP_B = '''012 Test B
022 Helsinki

001    1      Player, Abe                       2000
001    2      Player, Bea                       1900
'''

def test_create_groups() -> None:
    players = [
        Player('Tomi', 'Nybäck', '2614'),
        Player('Toivo', 'Keinänen', '2521'),
        Player('Abe', 'Player', '2000'),
        Player('Bea', 'Player', '1900')
    ]
    group_ends = [2, 4]
    expected = [
        {
            'data': GROUP_A,
            'player_count': 2
        },
        {
            'data': GROUP_B,
            'player_count': 2
        }
    ]
    trf = create_groups(players, group_ends, TOURNAMENT_INFO)
    assert trf == expected
