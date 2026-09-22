#!/usr/bin/env python3

import argparse

from trf.args import parse_args, validate_args, validate_groups
from trf.log import info, ok, warn
from trf.player import Player
from trf.players_parser import PlayersParser
from trf.rating_list import RatingList
from trf.trf import create_players, create_trf

def main(args: argparse.Namespace) -> None:
    if args.download_ratings:
        RatingList.download(args.ratings_file)
        ok(f'Fetched the latest ratings in {args.ratings_file}')
    else:
        handle_players(args)

def handle_players(args: argparse.Namespace) -> None:
    players = get_players(args)
    if (args.groups):
        validate_groups(args, len(players))
        create_trf(players, args.groups, args.tournament_file, args.output_dir)
    else:
        check_valid_players(players, args)
        list_players(players)

def get_players(args: argparse.Namespace) -> list[Player]:
    parser = PlayersParser()
    participants = parser.parse(args.players_file, header=not args.no_header)
    if args.exclude_ratings:
        return participants
    rating_list = RatingList(args.ratings_file)
    return rating_list.search(participants)

def check_valid_players(players: list[Player], args: argparse.Namespace) -> None:
    for p in players:
        if p.is_new:
            warn(f'Is new player: {p.name_club}')
        elif args.license and p.needs_license:
            warn(f'No license: {p.name_club}')

def list_players(players: list[Player]) -> None:
    trf = create_players(players, omit_id=True)
    print('\n'.join(trf))
    last_group = len(players)
    first_group = last_group // 2
    info(f'Create TRF: add the last player index of each group (--groups {first_group} {last_group})')

if __name__ == '__main__':
    main(validate_args(parse_args()))
