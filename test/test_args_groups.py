import argparse
import pytest
from pytest import CaptureFixture

from trf.args import parse_args, validate_groups

GROUPS_ARG = ['--groups', '16', '32']

def test_validate_groups_add_last_value(capsys: CaptureFixture[str]) -> None:
    args = [GROUPS_ARG[0], '16']
    player_count = 32
    parsed = assert_args_ok(
        capsys,
        args,
        player_count
    )
    assert parsed.groups == [16, player_count]

def test_validate_groups_last_value(capsys: CaptureFixture[str]) -> None:
    player_count = 31
    assert_args_msg(
        capsys,
        [GROUPS_ARG[0], '16', str(player_count + 1)],
        f'last number can not be > {player_count}',
        player_count
    )

@pytest.mark.parametrize('index', ['nonnumeric', '16.5'])
def test_validate_groups_int(capsys: CaptureFixture[str], index: str) -> None:
    assert_args_msg(
        capsys,
        [GROUPS_ARG[0], index],
        'invalid int value'
    )

def test_validate_groups_order(capsys: CaptureFixture[str]) -> None:
    assert_args_msg(
        capsys,
        [GROUPS_ARG[0], '32', '16'],
        'ascending order'
    )

def assert_args_ok(capsys: CaptureFixture[str], args: list[str], groups_count) -> argparse.Namespace:
    parsed = parse_args(args)
    validate_groups(parsed, groups_count)
    output = capsys.readouterr()
    assert output.err == '' and output.out == ''
    return parsed

def assert_args_msg(capsys: CaptureFixture[str], args: list[str], expected: str, groups_count = 0) -> None:
    with pytest.raises(SystemExit) as exit_msg:
        validate_groups(parse_args(args), groups_count)
    output = capsys.readouterr()
    assert expected in output.err or expected in output.out or expected in str(exit_msg.value)
