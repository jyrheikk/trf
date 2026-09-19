import argparse
from pathlib import Path

from trf.log import fatal

INPUT_DIR = 'data/input'

DEFAULT_TOURNAMENT_FILE = f'{INPUT_DIR}/tournament.trf'

DEFAULT_PLAYERS_FILE = f'{INPUT_DIR}/players.csv'

RATINGS_FILE = f'{INPUT_DIR}/selolista.csv'

def parse_args(argv = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='trf',
        description='Create Tournament Report Files (TRF) for a chess tournament'
    )

    download = parser.add_argument_group('download ratings')
    download.add_argument(
        '-d', '--download-ratings',
        action='store_true',
        help=f'download the latest {RATINGS_FILE}'
    )

    create = parser.add_argument_group('create Tournament Report Files')
    create.add_argument(
        '-g', '--groups',
        type=int,
        metavar='INDEX',
        nargs='*',
        help='indexes of the last player in each group'
    )
    create.add_argument(
        '-n', '--no-header',
        action='store_true',
        help='do not skip the first line of the players file'
    )
    create.add_argument(
        '-l', '--license',
        action='store_true',
        help='list players without license'
    )
    create.add_argument(
        '-p', '--players',
        type=str,
        metavar='PLAYERS_CSV',
        default=DEFAULT_PLAYERS_FILE,
        help=f'name of the players CSV file (default {DEFAULT_PLAYERS_FILE})'
    )
    create.add_argument(
        '-t', '--tournament',
        type=str,
        metavar='TOURNAMENT_TRF',
        default=DEFAULT_TOURNAMENT_FILE,
        help=f'name of the Tournament Report File (default {DEFAULT_TOURNAMENT_FILE})'
    )
    create.add_argument(
        '-w', '--without-ratings',
        action='store_true',
        help='create players without ratings'
    )

    return parser.parse_args(argv)

def validate_args(args: argparse.Namespace) -> argparse.Namespace:
    if args.players:
        assert_file(args.players)
    if args.tournament:
        assert_file(args.tournament)

    return args

def validate_groups(args: argparse.Namespace, count: int) -> None:
    sorted_arr = sorted(args.groups, key=int)
    sorted_values = to_str(sorted_arr)
    values = to_str(args.groups)
    if sorted_values != values:
        fatal(f'Give options in the ascending order: --groups {values}')
    elif args.groups[-1] > count:
        fatal(f'--groups option: the last number can not be > {count}')
    elif count not in args.groups:
        args.groups.append(count)

def assert_file(filename: str) -> None:
    file_path = Path(filename)
    if not file_path.exists():
        fatal(f'File not found: {filename}')

def to_str(arr: list[int]) -> str:
    return ' '.join(map(str, arr))
