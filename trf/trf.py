import os
from pathlib import Path
from string import ascii_uppercase as ASCII

from trf.log import ok
from trf.player import Player

GROUP_ID = '{GROUP}'

TRF_PLAYER_TAG = '001'

def create_trf(players: list[Player], group_ends: list[int], tournament: str, output_dir: str) -> None:
    with open(tournament) as file:
        tournament_info = file.read()
    groups = create_groups(players, group_ends, tournament_info)
    for i, group in enumerate(groups):
        filename = f'{output_dir}/tournament-{ASCII[i]}.trf'
        if i == 0:
            create_directory(filename)
        with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write(group['data'])
            ok(f'Created {filename} ({group['player_count']} players)')

def create_groups(players: list[Player], group_ends: list[int], tournament_info: str) -> None:
    trf = []
    first_player = 0
    for i, last_player in enumerate(group_ends):
        group_players = players[first_player:last_player]
        players_trf = create_players(group_players)
        group = (
            tournament_info.replace(GROUP_ID, ASCII[i]) +
            '\n' +
            '\n'.join(players_trf) +
            '\n'
        )
        trf.append({
            'data': group,
            'player_count': last_player - first_player
        })
        first_player = last_player
    return trf

def create_players(players: list[Player], omit_id = False) -> str:
    trf = []
    for i, p in enumerate(players):
        trf.append(__format_player(p, i + 1, omit_id))
    return trf

def __format_player(player: Player, index: int, omit_id) -> str:
    id_field = '' if omit_id else f'{TRF_PLAYER_TAG:<7}'
    return f'{id_field}{index:<7}{player.name:<34}{player.rating}'

def create_directory(filename: str) -> None:
    parent = Path(filename).parent
    if not os.path.exists(parent):
        os.makedirs(parent)
