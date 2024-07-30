import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

# Фикстуры для значений, используемых в тестах
@pytest.fixture
def capitalize_cases():
    return [
        ("minsk", "Minsk"),
        ("Minsk", "Minsk"),
        ("hello world", "Hello world"),
        ("", ""),
        (" ", " "),
        ("0000sever", "0000sever"),
    ]

@pytest.fixture
def trim_cases():
    return [
        (" summer", "summer"),
        (" Hello summer ", "Hello summer "),
        ("", ""),
        ("    ", ""),
    ]

@pytest.fixture
def to_list_cases():
    return [
        ("S,O,N", ["S", "O", "N"]),
        ("2:2:2", ":", ["2", "2", "2"]),
        ("", ",", []),
        ("SON", ",", ["SON"]),
        (":2:2:2:", ":", ["", "2", "2", "2", ""]),
    ]

@pytest.fixture
def contains_cases():
    return [
        ("skypro", "s", True),
        ("holidays", "a", True),
        ("skypro", "u", False),
    ]

@pytest.fixture
def delete_symbol_cases():
    return [
        ("skypro", "k", "sypro"),
        ("skypro", "pro", "sky"),
        ("the sun", "moon", "the sun"),
    ]

@pytest.fixture
def starts_with_cases():
    return [
        ("grin", "g", True),
        ("grin", "n", False),
        ("grin", "grin", True),
        ("grin", "green", False),
    ]

@pytest.fixture
def ends_with_cases():
    return [
        ("кошка", "а", True),
        ("кошка", "ка", True),
        ("кошка", "кошка", True),
        ("", "a", False),
    ]

@pytest.fixture
def is_empty_cases():
    return [
        ("", True),
        (" ", True),
        ("//n", False),
        ("skypro", False),
    ]

@pytest.fixture
def list_to_string_cases():
    return [
        ([1, 2, 3, 4], "1, 2, 3, 4"),
        (["sky", "pro"], "sky, pro"),
        (["sky", "pro"], "-", "sky-pro"),
        ([], ""),
        (["single"], "single"),
    ]

# Tests for capitalize
def test_capitalize(utils, capitalize_cases):
    for input_str, expected in capitalize_cases:
        assert utils.capitalize(input_str) == expected

# Tests for trim
def test_trim(utils, trim_cases):
    for input_str, expected in trim_cases:
        assert utils.trim(input_str) == expected

# Tests for to_list
def test_to_list(utils, to_list_cases):
    for input_str, delimiter, expected in to_list_cases:
        assert utils.to_list(input_str, delimiter) == expected

# Tests for contains
def test_contains(utils, contains_cases):
    for string, char, expected in contains_cases:
        assert utils.contains(string, char) == expected

# Tests for delete_symbol
def test_delete_symbol(utils, delete_symbol_cases):
    for string, symbol, expected in delete_symbol_cases:
        assert utils.delete_symbol(string, symbol) == expected

# Tests for starts_with
def test_starts_with(utils, starts_with_cases):
    for string, prefix, expected in starts_with_cases:
        assert utils.starts_with(string, prefix) == expected

# Tests for ends_with
def test_ends_with(utils, ends_with_cases):
    for string, suffix, expected in ends_with_cases:
        assert utils.ends_with(string, suffix) == expected

# Tests for is_empty
def test_is_empty(utils, is_empty_cases):
    for input_str, expected in is_empty_cases:
        assert utils.is_empty(input_str) == expected

# Tests for list_to_string
def test_list_to_string(utils, list_to_string_cases):
    for input_list, expected in list_to_string_cases:
        assert utils.list_to_string(input_list) == expected