from trf.player import Player
from trf.rated_players import RatedPlayers

def test_search_all() -> None:
    rated = RatedPlayers()
    registrants = [
        Player('Jyrki', 'Heikkinen', '', 'LauttSSK')
    ]
    result = rated.search_all(registrants)
    assert len(result) == 1
    p = result[0]
    assert p.first_name == 'Jyrki' and p.rating > '2000' and p.rating < '2120'
