import argparse
import sys

DEFAULT_TOURNAMENT_FILE = 'tournament.trf'

DEFAULT_PLAYERS_FILE = 'players.csv'

RATINGS_FILE = 'selolista.csv'

def parse_args(argv = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='trf',
        description='Create Tournament Report File for a chess tournament'
    )

    download = parser.add_argument_group('download')
    download.add_argument(
        '-d', '--download-ratings',
        action='store_true',
        help=f'download the latest {RATINGS_FILE}'
    )

    create = parser.add_argument_group('create')
    create.add_argument(
        '-g', '--group_ends',
        type=int,
        metavar='INDEX',
        nargs='*',
        help='indexes of the last player in each group'
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

    return parser.parse_args(argv)

def validate_args(args: argparse.Namespace) -> argparse.Namespace:
    if args.group_ends:
        sorted_arr = sorted(args.group_ends, key=int)
        sorted_values = to_str(sorted_arr)
        values = to_str(args.group_ends)
        if sorted_values != values:
            sys.exit(f'❌ give arguments in the ascending order: --group_ends {values}')

    return args

def to_str(arr: list[int]) -> str:
    return ' '.join(map(str, arr))
