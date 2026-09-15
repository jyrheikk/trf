import pytest
from pytest import CaptureFixture

from trf.args import parse_args, validate_args

DOWNLOAD_ARG = ['--download-ratings']
GROUP_ENDS_ARG = ['--group-ends', '16', '32']
PLAYERS_ARG = ['--players', 'test/data/test-players.csv']
TOURNAMENT_ARG = ['--tournament', 'data/samples/tournament.trf']

@pytest.mark.parametrize('option', ['-h', '--help'])
def test_validate_args_show_help(capsys: CaptureFixture[str], option: str) -> None:
    assert_args_msg(
        capsys,
        [option],
        'show this help message'
    )

def test_validate_args_create_tournament_succeeds(capsys: CaptureFixture[str]) -> None:
    assert_args_ok(
        capsys,
        [*GROUP_ENDS_ARG, *PLAYERS_ARG, *TOURNAMENT_ARG]
    )

@pytest.mark.parametrize('index', ['nonnumeric', '16.5'])
def test_validate_args_group_ends_int(capsys: CaptureFixture[str], index: str) -> None:
    assert_args_msg(
        capsys,
        [GROUP_ENDS_ARG[0], index],
        'invalid int value'
    )

def test_validate_args_group_ends_order(capsys: CaptureFixture[str]) -> None:
    assert_args_msg(
        capsys,
        [GROUP_ENDS_ARG[0], '32', '16'],
        'ascending order'
    )

@pytest.mark.parametrize('filename', ['non-existing-file.csv'])
def test_validate_args_filename(capsys: CaptureFixture[str], filename: str) -> None:
    assert_args_msg(
        capsys,
        [PLAYERS_ARG[0], filename],
        f'File not found: {filename}'
    )

@pytest.mark.parametrize('option', ['--unknown-arg'])
def test_validate_args_create_unknown_arg(capsys: CaptureFixture[str], option: str) -> None:
    assert_args_msg(
        capsys,
        [option],
        f'unrecognized arguments: {option}'
    )

def assert_args_ok(capsys: CaptureFixture[str], args: list[str]) -> None:
    validate_args(parse_args(args))
    output = capsys.readouterr()
    assert output.err == '' and output.out == ''

def assert_args_msg(capsys: CaptureFixture[str], args: list[str], expected: str) -> None:
    with pytest.raises(SystemExit) as exit_msg:
        validate_args(parse_args(args))
    output = capsys.readouterr()
    assert expected in output.err or expected in output.out or expected in str(exit_msg.value)
