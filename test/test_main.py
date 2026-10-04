from pytest import CaptureFixture

from trf.__main__ import main
from trf.args import parse_args

ARGS = [
    *['--players-file', 'test/data/test-players.csv'],
    *['--ratings-file', 'test/data/test-ratings.csv'],
    '--license'
]

def test_list_players(capsys: CaptureFixture[str]) -> None:
    main(parse_args(ARGS))
    output = capsys.readouterr()
    expected = [
        'No license: Casual, John (MatSK)',
        'Is new player: Player, New',
        '1      Heikkinen, Jyrki                  2047',
        '2      Casual, John                      1558',
        '3      Player, New                       1425',
        "4      D'Amato, Carolina                 1409",
        '5      Beginner-Novice Starter, Really L 1298',
        '(--groups 2 5)'
    ]
    for row in expected:
        assert row in output.out

def test_list_given_players(capsys: CaptureFixture[str]) -> None:
    args = [
        *['--ratings-file', 'test/data/test-ratings.csv'],
        *['--find-players', 'Dyral,Dody,Int', 'Dzyura,Khristofor']
    ]
    main(parse_args(args))
    output = capsys.readouterr()
    expected = [
        '1      Dzyura, Khristofor                1602',
        '2      Dyral, Dody                       1517'
    ]
    for row in expected:
        assert row in output.out

def test_create_tournament(capsys: CaptureFixture[str]) -> None:
    args = [
        *ARGS,
        *['--info-file', 'samples/classical-info.trf'],
        *['--output-dir', 'test/data/output'],
        *['--groups', '2']
    ]
    main(parse_args(args))
    output = capsys.readouterr()
    expected = [
        'Created test/data/output/tournament-A.trf (2 players)',
        'Created test/data/output/tournament-B.trf (3 players)'
    ]
    for row in expected:
        assert row in output.out
