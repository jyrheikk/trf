#!/usr/bin/env python3

import argparse

from trf.args import parse_args, validate_args
from trf.csv import parse_csv
from trf.log import fatal, info, warn
from trf.player import Player
from trf.rated_players import RatedPlayers
from trf.trf import create_players, create_trf

def main(args: argparse.Namespace) -> None:
    if args.download_ratings:
        RatedPlayers.download()
    else:
        handle_players(args)

def handle_players(args: argparse.Namespace) -> None:
    players = get_players(args)
    if (args.groups):
        validate_groups(args, len(players))
        create_trf(players, args.groups, args.tournament)
    else:
        list_players(players)

def get_players(args: argparse.Namespace) -> list[Player]:
    rated_players = RatedPlayers()
    participants = parse_csv(args.players, skip_header=not args.no_header)
    return rated_players.search_all(participants)

def validate_groups(args: argparse.Namespace, count: int) -> None:
    if args.groups[-1] > count:
        fatal(f'--groups option: the last number can not be > {count}')
    elif count not in args.groups:
        args.groups.append(count)

def list_players(players: list[Player]) -> None:
    trf = create_players(players)
    print('\n'.join(trf))
    check_new_players(players)
    last_group = len(players)
    first_group = last_group // 2
    info(f'Create TRF: add the last player index of each group (--groups {first_group} {last_group})')

def check_new_players(players: list[Player]) -> None:
    for p in players:
        if p.is_new:
            warn(f'Check if this is a new player: {p.search_name}')

if __name__ == '__main__':
    main(validate_args(parse_args()))
