from pytest import CaptureFixture

from trf.__main__ import main
from trf.args import parse_args

EXPECTED_OUTPUT = [
    '1      Heikkinen, Jyrki                  2064',
    'Create TRF: add the last player index of each group (--groups 0 1)'
]

def test_list_players(capsys: CaptureFixture[str]) -> None:
    args = ['--players', 'test/data/test-players.csv']
    main(parse_args(args))
    output = capsys.readouterr()
    for row in EXPECTED_OUTPUT:
        assert row in output.out
