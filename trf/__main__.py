#!/usr/bin/env python3

import argparse

from trf.args import parse_args, validate_args
from trf.csv import parse_registrants
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
    registrants = parse_registrants(args.players)
    info(f'#registrants: {len(registrants)}')
    rated_players = RatedPlayers.parse()
    info(f'#players in selolista: {len(rated_players)}')
    players = get_all_players(registrants, rated_players)
    sorted_players = RatedPlayers.sort_by_rating(players)
    if (args.group_ends):
        create_trf(sorted_players, args.group_ends, args.tournament or None)
    else:
        trf = create_players(sorted_players)
        print('\n'.join(trf))
        info('Create TRF: add the last player index of each group (--group-ends 12 24)')

def get_all_players(registrants: list[Player], rated_players: list[Player]) -> list[Player]:
    players = []
    for reg in registrants:
        player = reg.search(rated_players)
        if player:
            players.append(player)
        else:
            warn(f'Check if this is a new player: {reg.search_name}')
            players.append(Player(reg.first_name, reg.last_name))
    return players

if __name__ == '__main__':
    main(validate_args(parse_args()))
