from pytest import CaptureFixture

from trf.__main__ import main
from trf.args import parse_args

EXPECTED_OUTPUT = [
    'Is new player: Player, Random',
    '1      Heikkinen, Jyrki                  2047',
    '2      Player, Random                    1525',
    '(--groups 1 2)'
]

def test_list_players(capsys: CaptureFixture[str]) -> None:
    args = [
        '--players',
        'test/data/test-players.csv',
        '--ratings',
        'test/data/test-ratings.csv',
    ]
    main(parse_args(args))
    output = capsys.readouterr()
    for row in EXPECTED_OUTPUT:
        assert row in output.out
