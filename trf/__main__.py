#!/usr/bin/env python3

import argparse

from trf.args import parse_args, validate_args, validate_groups
from trf.csv import parse_csv
from trf.log import info, ok, warn
from trf.player import Player
from trf.rated_players import RatedPlayers
from trf.trf import create_players, create_trf

def main(args: argparse.Namespace) -> None:
    if args.download_ratings:
        RatedPlayers.download(args.ratings_file)
        ok(f'Fetched the latest ratings in {args.ratings_file}')
    else:
        handle_players(args)

def handle_players(args: argparse.Namespace) -> None:
    players = get_players(args)
    if (args.groups):
        validate_groups(args, len(players))
        create_trf(players, args.groups, args.tournament_file)
    else:
        check_valid_players(players, args)
        list_players(players)

def get_players(args: argparse.Namespace) -> list[Player]:
    participants = parse_csv(args.players_file, skip_header=not args.no_header)
    if args.without_ratings:
        return participants
    rated_players = RatedPlayers(args.ratings_file)
    return rated_players.search_all(participants)

def check_valid_players(players: list[Player], args: argparse.Namespace) -> None:
    for p in players:
        if p.is_new:
            warn(f'Is new player: {p.name_club}')
        elif args.license and not p.has_license:
            warn(f'No license: {p.name_club}')

def list_players(players: list[Player]) -> None:
    trf = create_players(players, omit_id=True)
    print('\n'.join(trf))
    last_group = len(players)
    first_group = last_group // 2
    info(f'Create TRF: add the last player index of each group (--groups {first_group} {last_group})')

if __name__ == '__main__':
    main(validate_args(parse_args()))
