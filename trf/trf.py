import os

from trf.log import ok
from trf.player import Player

OUTPUT_DIR = 'data/output'

TRF_PLAYER_ID = '001'

def create_trf(players: list[Player], groups: list[int], tournament: str) -> None:
    with open(tournament) as file:
        tournament_info = file.read()
    create_directory(OUTPUT_DIR)
    first_player = 0
    for index, last_player in enumerate(groups):
        filename = f'{OUTPUT_DIR}/tournament-{index + 1}.trf'
        with open(filename, 'w', encoding='utf-8') as outfile:
            group_players = players[first_player:last_player]
            players_trf = create_players(group_players)
            data = (
                tournament_info +
                '\n' +
                '\n'.join(players_trf) +
                '\n'
            )
            outfile.write(data)
            ok(f'Created {filename} ({last_player - first_player} players)')
            first_player = last_player

def create_players(players: list[Player]) -> str:
    trf = []
    for index, p in enumerate(players):
        trf.append(__format_player(p, index + 1))
    return trf

def __format_player(player: Player, index: int) -> str:
    name = f'{player.last_name}, {player.first_name}'
    return f'{TRF_PLAYER_ID:<7}{index:<7}{name:<34}{player.rating}'

def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
