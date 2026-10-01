import os
from pathlib import Path
from string import ascii_uppercase as ASCII

from trf.log import ok
from trf.player import Player

TRF_PLAYER_TAG = '001'
SEX = ''
TITLE = ''
GROUP_ID = '{GROUP}'

class TournamentReportFile:
    def __init__(self, players: list[Player], exclude_ratings = False):
        self.players = players
        self.exclude_ratings = exclude_ratings

    def create_tournament(self, group_ends: list[int], tournament: str, output_dir: str) -> None:
        with open(tournament) as file:
            tournament_info = file.read()
        groups = self.create_groups(group_ends, tournament_info)
        for i, group in enumerate(groups):
            filename = f'{output_dir}/tournament-{ASCII[i]}.trf'
            if i == 0:
                self.create_directory(filename)
            with open(filename, 'w', encoding='utf-8') as outfile:
                outfile.write(group['data'])
                ok(f'Created {filename} ({group['player_count']} players)')

    def create_groups(self, group_ends: list[int], tournament_info: str) -> None:
        trf = []
        first_player = 0
        for i, last_player in enumerate(group_ends):
            group_players = self.players[first_player:last_player]
            players_trf = self.create_players(group_players)
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

    def create_players(self, players: list[Player], omit_id = False) -> str:
        trf = []
        for i, p in enumerate(players):
            trf.append(self.format_player(p, i + 1, omit_id))
        return trf

    def format_player(self, player: Player, index: int, omit_id) -> str:
        tag = '' if omit_id else f'{TRF_PLAYER_TAG:<3}'
        rating = '' if self.exclude_ratings else f'{player.rating:>4}'
        return (
            f'{tag} {index:>4} '
            f'{SEX:<1}{TITLE:<3} '
            f'{player.name[0:33]:<33} {rating}'
        )

    @staticmethod
    def create_directory(filename: str) -> None:
        parent = Path(filename).parent
        if not os.path.exists(parent):
            os.makedirs(parent)
