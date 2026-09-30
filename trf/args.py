import argparse
from pathlib import Path

from trf.log import fatal

DEFAULT_PLAYERS_FILE = 'players.csv'
DEFAULT_RATINGS_FILE = 'selolista.csv'
DEFAULT_TOURNAMENT_FILE = 'tournament.trf'

def parse_args(argv = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='trf',
        description='Create Tournament Report Files (TRF) for a chess tournament'
    )

    download = parser.add_argument_group('download ratings')
    download.add_argument(
        '-d', '--download-ratings',
        action='store_true',
        help='download the latest rating file'
    )

    players = parser.add_argument_group('list players')
    players.add_argument(
        '-e', '--exclude-ratings',
        action='store_true',
        help='skip searching players from the rating file'
    )
    players.add_argument(
        '-f', '--find-players',
        type=str,
        metavar='LAST,FIRST[,CLUB]',
        nargs='*',
        help='find the given players from the rating file'
    )
    players.add_argument(
        '-l', '--license',
        action='store_true',
        help='list players without license'
    )
    players.add_argument(
        '-n', '--no-header',
        action='store_true',
        help='do not skip the first line of the players file'
    )

    create = parser.add_argument_group('create Tournament Report Files (and list players options)')
    create.add_argument(
        '-g', '--groups',
        type=int,
        metavar='INDEX',
        nargs='*',
        help='indexes of the last player in each group'
    )

    testing = parser.add_argument_group('testing options')
    testing.add_argument(
        '-o', '--output-dir',
        type=str,
        metavar='DIRECTORY',
        default='.',
        help='name of the output directory for tournament TRF files (default is the current directory)'
    )
    testing.add_argument(
        '-p', '--players-file',
        type=str,
        metavar='PLAYERS.CSV',
        default=DEFAULT_PLAYERS_FILE,
        help=f'name of the players CSV file (default {DEFAULT_PLAYERS_FILE})'
    )
    testing.add_argument(
        '-r', '--ratings-file',
        type=str,
        metavar='RATINGS.CSV',
        default=DEFAULT_RATINGS_FILE,
        help=f'name of the ratings CSV file (default {DEFAULT_RATINGS_FILE})'
    )
    testing.add_argument(
        '-t', '--tournament-file',
        type=str,
        metavar='TOURNAMENT.TRF',
        default=DEFAULT_TOURNAMENT_FILE,
        help=f'name of the Tournament Report File (default {DEFAULT_TOURNAMENT_FILE})'
    )

    return parser.parse_args(argv)

def validate_args(args: argparse.Namespace) -> argparse.Namespace:
    if not args.download_ratings:
        assert_file(args.players_file)
    if args.groups:
        assert_file(args.tournament_file)

def assert_file(filename: str) -> None:
    if filename:
        file_path = Path(filename)
        if not file_path.exists():
            fatal(f'File not found: {filename}')

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

def to_str(arr: list[int]) -> str:
    return ' '.join(map(str, arr))
