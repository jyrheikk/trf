from pytest import CaptureFixture

from trf.__main__ import main
from trf.args import parse_args

EXPECTED_OUTPUT = [
    'No license: Casual, John (MatSK)',
    'Is new player: Player, New',
    '1      Heikkinen, Jyrki                  2047',
    '2      Casual, John                      1558',
    '3      Player, New                       1525',
    '4      Beginner, Real                    1298',
    '(--groups 2 4)'
]

def test_list_players(capsys: CaptureFixture[str]) -> None:
    args = [
        '--players',
        'test/data/test-players.csv',
        '--ratings',
        'test/data/test-ratings.csv',
        '--license'
    ]
    main(parse_args(args))
    output = capsys.readouterr()
    for row in EXPECTED_OUTPUT:
        assert row in output.out
