#!/usr/bin/env python3

import argparse
import urllib.request

from trf.args import RATINGS_FILE, parse_args, validate_args
from trf.csv import parse_rated_players, parse_registrants
from trf.trf import create_players
from trf.player import Player

def main(args: argparse.Namespace) -> None:
    if args.download_ratings:
        download_ratings()
    elif args.players:
        create_players_trf(args.players)

def download_ratings():
    url = f'https://www.shakki.net/selo/{RATINGS_FILE}'

    with urllib.request.urlopen(url) as response:
        content = response.read().decode('latin-1')

    with open(RATINGS_FILE, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def create_players_trf(players_file) -> None:
    registrants = parse_registrants(players_file)
    print(f'#registrants: {len(registrants)}')
    rated_players = parse_rated_players()
    print(f'#players in selolista: {len(rated_players)}')
    players = []
    for reg in registrants:
        player = search_player(reg, rated_players)
        if player:
            players.append(player)
        else:
            club = '({reg.club})' if reg.club else ''
            print(f'⚠️  Check if this is a new player: {reg.last_name}, {reg.first_name} {club}')
            players.append(Player(reg.first_name, reg.last_name))
    sorted_players = sorted(players, key=lambda p: p.rating, reverse=True)
    trf = create_players(sorted_players)
    print('\n'.join(trf))
    print('✅ TRF created')

def search_player(registrant: Player, rated_players: list[Player]) -> Player:
    for rated in rated_players:
        if registrant.equals(rated):
            return rated

if __name__ == '__main__':
    main(validate_args(parse_args()))
