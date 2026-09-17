#!/usr/bin/env python3

import argparse

from trf.args import parse_args, validate_args
from trf.csv import parse_participants
from trf.log import info, warn
from trf.player import Player
from trf.rated_players import RatedPlayers
from trf.trf import create_players, create_trf

def main(args: argparse.Namespace) -> None:
    if args.download_ratings:
        RatedPlayers.download()
    else:
        create_players_trf(args)

def create_players_trf(args: argparse.Namespace) -> None:
    rated_players = RatedPlayers()
    participants = parse_participants(args.players)
    players = rated_players.search_all(participants)
    if (args.groups):
        create_trf(players, args.groups, args.tournament or None)
    else:
        trf = create_players(players)
        print('\n'.join(trf))
        check_new_players(players)
        info('Create TRF: add the last player index of each group (-g 12 24)')

def check_new_players(players: list[Player]) -> None:
    for p in players:
        if p.is_new:
            warn(f'Check if this is a new player: {p.search_name}')

if __name__ == '__main__':
    main(validate_args(parse_args()))
