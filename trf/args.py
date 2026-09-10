import argparse

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
        '-g', '--groups',
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
    return args
