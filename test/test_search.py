from trf.search import binary_search

TEST_DATA = [
    {'name': 'a'},
    {'name': 'b'},
    {'name': 'c'},
    {'name': 'd'},
    {'name': 'e'},
    {'name': 'f'},
    {'name': 'g'},
    {'name': 'h'},
]

def test_binary_search_found() -> None:
    result = binary_search(TEST_DATA, 'g', key=lambda x: x['name'])
    assert result == 6

def test_binary_search_not_found() -> None:
    result = binary_search(TEST_DATA, 'foo', key=lambda x: x['name'])
    assert result == -1
