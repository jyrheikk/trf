from pytest import CaptureFixture

from trf.__main__ import main
from trf.args import parse_args

EXPECTED_LIST_OUTPUT = [
    'No license: Casual, John (MatSK)',
    'Is new player: Player, New',
    '1      Heikkinen, Jyrki                  2047         501301',
    '2      Casual, John                      1558',
    '3      Player, New                       1425',
    '4      Beginner, Real                    1298',
    '(--groups 2 4)'
]

ARGS = [
    '--players-file',
    'test/data/test-players.csv',
    '--ratings-file',
    'test/data/test-ratings.csv',
    '--license'
]

def test_list_players(capsys: CaptureFixture[str]) -> None:
    main(parse_args(ARGS))
    output = capsys.readouterr()
    for row in EXPECTED_LIST_OUTPUT:
        assert row in output.out

def test_create_tournament(capsys: CaptureFixture[str]) -> None:
    args = [
        *ARGS,
        '--output-dir',
        'test/data/output',
        '--groups',
        '2'
    ]
    main(parse_args(args))
    output = capsys.readouterr()
    expected = [
        'Created test/data/output/tournament-A.trf (2 players)',
        'Created test/data/output/tournament-B.trf (2 players)'
    ]
    for row in expected:
        assert row in output.out
