from trf.player import Player

def test_set_needs_license() -> None:
    p = Player('random', 'surname')
    p.set_needs_license()
    assert p.needs_license
