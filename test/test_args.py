import argparse
import pytest
from pytest import CaptureFixture

from trf.args import parse_args, validate_args

DOWNLOAD_ARG = ['--download-ratings']
GROUPS_ARG = ['--groups', '16', '32']
NO_HEADER_ARG = ['--no-header']
PLAYERS_ARG = ['--players', 'test/data/test-players.csv']
TOURNAMENT_ARG = ['--tournament', 'data/samples/tournament.trf']
WITHOUT_RATINGS_ARG = ['--without-ratings']

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
        [*GROUPS_ARG, *NO_HEADER_ARG, *PLAYERS_ARG, *TOURNAMENT_ARG, *WITHOUT_RATINGS_ARG],
        32
    )

def test_validate_args_groups_add_last_value(capsys: CaptureFixture[str]) -> None:
    args = [GROUPS_ARG[0], '16']
    player_count = 32
    parsed = assert_args_ok(
        capsys,
        args,
        player_count
    )
    assert parsed.groups == [16, player_count]

@pytest.mark.parametrize('index', ['nonnumeric', '16.5'])
def test_validate_args_groups_int(capsys: CaptureFixture[str], index: str) -> None:
    assert_args_msg(
        capsys,
        [GROUPS_ARG[0], index],
        'invalid int value'
    )

def test_validate_args_groups_order(capsys: CaptureFixture[str]) -> None:
    assert_args_msg(
        capsys,
        [GROUPS_ARG[0], '32', '16'],
        'ascending order'
    )

def test_validate_args_groups_last_value(capsys: CaptureFixture[str]) -> None:
    player_count = 31
    assert_args_msg(
        capsys,
        [GROUPS_ARG[0], '16', str(player_count + 1)],
        f'last number can not be > {player_count}',
        player_count
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

def assert_args_ok(capsys: CaptureFixture[str], args: list[str], groups_count) -> argparse.Namespace:
    parsed = parse_args(args)
    validate_args(parsed, groups_count)
    output = capsys.readouterr()
    assert output.err == '' and output.out == ''
    return parsed

def assert_args_msg(capsys: CaptureFixture[str], args: list[str], expected: str, groups_count = 0) -> None:
    with pytest.raises(SystemExit) as exit_msg:
        validate_args(parse_args(args), groups_count)
    output = capsys.readouterr()
    assert expected in output.err or expected in output.out or expected in str(exit_msg.value)
