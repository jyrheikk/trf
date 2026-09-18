from trf.player import Player
from trf.trf import create_groups

def test_create_groups() -> None:
    players = [
        Player('Tomi', 'Nybäck', '2614'),
        Player('Toivo', 'Keinänen', '2521'),
        Player('Abe', 'Player', '2000'),
        Player('Bea', 'Player', '1900')
    ]
    group_ends = [2, 4]
    tournament_info = (
        '012 Test {GROUP}\n'
        '022 Helsinki\n'
    )
    expected = [
        {
            'data': (
                '012 Test A\n'
                '022 Helsinki\n'
                '\n'
                '001    1      Nybäck, Tomi                      2614\n'
                '001    2      Keinänen, Toivo                   2521\n'
            ),
            'player_count': 2
        },
        {
            'data': (
                '012 Test B\n'
                '022 Helsinki\n'
                '\n'
                '001    1      Player, Abe                       2000\n'
                '001    2      Player, Bea                       1900\n'
            ),
            'player_count': 2
        }
    ]
    trf = create_groups(players, group_ends, tournament_info)
    assert trf == expected
