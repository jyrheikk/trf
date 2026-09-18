import os
from string import ascii_uppercase as ASCII


from trf.log import ok
from trf.player import Player

OUTPUT_DIR = 'data/output'

GROUP_ID = '{GROUP}'

TRF_PLAYER_ID = '001'

def create_trf(players: list[Player], groups: list[int], tournament: str) -> None:
    with open(tournament) as file:
        tournament_info = file.read()
    create_directory(OUTPUT_DIR)
    first_player = 0
    for i, last_player in enumerate(groups):
        filename = f'{OUTPUT_DIR}/tournament-{ASCII[i]}.trf'
        with open(filename, 'w', encoding='utf-8') as outfile:
            group_players = players[first_player:last_player]
            players_trf = create_players(group_players)
            data = (
                tournament_info.replace(GROUP_ID, ASCII[i]) +
                '\n' +
                '\n'.join(players_trf) +
                '\n'
            )
            outfile.write(data)
            ok(f'Created {filename} ({last_player - first_player} players)')
            first_player = last_player

def create_players(players: list[Player], omit_id = False) -> str:
    trf = []
    for i, p in enumerate(players):
        trf.append(__format_player(p, i + 1, omit_id))
    return trf

def __format_player(player: Player, index: int, omit_id) -> str:
    name = f'{player.last_name}, {player.first_name}'
    id_field = '' if omit_id else f'{TRF_PLAYER_ID:<7}'
    return f'{id_field}{index:<7}{name:<34}{player.rating}'

def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
