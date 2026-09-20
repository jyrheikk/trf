import pytest
from pytest import CaptureFixture

from trf.args import parse_args, validate_args

@pytest.mark.parametrize('option', ['-h', '--help'])
def test_validate_args_show_help(capsys: CaptureFixture[str], option: str) -> None:
    assert_args_msg(
        capsys,
        [option],
        'show this help message'
    )

def test_validate_args_download_ratings_succeeds(capsys: CaptureFixture[str]) -> None:
    assert_args_ok(
        capsys,
        [
            '--download-ratings',
            *['--ratings-file', 'test/data/test-ratings.csv']
        ]
    )

def test_validate_args_list_players_succeeds(capsys: CaptureFixture[str]) -> None:
    assert_args_ok(
        capsys,
        [
            '--exclude-ratings',
            '--license',
            '--no-header',
            *['--players-file', 'test/data/test-players.csv']
        ]
    )

def test_validate_args_create_tournament_succeeds(capsys: CaptureFixture[str]) -> None:
    assert_args_ok(
        capsys,
        [
            *['--groups', '16', '32'],
            *['--output-dir', 'test/data/output'],
            *['--tournament-file', 'data/samples/tournament.trf']
        ]
    )

@pytest.mark.parametrize('filename', ['non-existing-file.csv'])
def test_validate_args_filename(capsys: CaptureFixture[str], filename: str) -> None:
    assert_args_msg(
        capsys,
        ['--players-file', filename],
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
