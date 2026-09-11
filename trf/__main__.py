#!/usr/bin/env python3

import argparse
import urllib.request

from trf.args import RATINGS_FILE, parse_args, validate_args
from trf.csv import parse_rated_players, parse_registrants
from trf.log import info, warn
from trf.player import Player
from trf.search import binary_search
from trf.trf import create_players, create_trf

def main(args: argparse.Namespace) -> None:
    if args.download_ratings:
        download_ratings()
    else:
        create_players_trf(args)

def download_ratings():
    url = 'https://www.shakki.net/selo/selolista.csv'

    with urllib.request.urlopen(url) as response:
        content = response.read().decode('latin-1')

    with open(RATINGS_FILE, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def create_players_trf(args: argparse.Namespace) -> None:
    registrants = parse_registrants(args.players)
    print(f'#registrants: {len(registrants)}')
    rated_players = parse_rated_players(RATINGS_FILE)
    print(f'#players in selolista: {len(rated_players)}')
    players = get_all_players(registrants, rated_players)
    sorted_players = sorted(players, key=lambda p: p.rating, reverse=True)
    if (args.group_ends):
        create_trf(sorted_players, args.group_ends, args.tournament or None)
    else:
        trf = create_players(sorted_players)
        print('\n'.join(trf))
        info('Create TRF: add the last player index of each group (--group-ends 12 24)')

def get_all_players(registrants: list[Player], rated_players: list[Player]) -> list[Player]:
    players = []
    for reg in registrants:
        player = search_player(reg, rated_players)
        if player:
            players.append(player)
        else:
            warn(f'Check if this is a new player: {reg.search_name}')
            players.append(Player(reg.first_name, reg.last_name))
    return players

def search_player(registrant: Player, rated_players: list[Player]) -> Player:
    i = binary_search(
        rated_players,
        registrant.search_name,
        key=lambda x: x.search_name
    )
    return rated_players[i]

if __name__ == '__main__':
    main(validate_args(parse_args()))
