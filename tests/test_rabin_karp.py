import pytest
from rabin_karp import rabin_karp_search


input_expected = [
    (('Test', 'testTesttesT'), [4]),
    (('aaaaa', 'baaaaaaa'), [1, 2, 3]),
    (('aba', 'abacaba'), [0, 4]),
]


@pytest.mark.parametrize('test_input, expected', input_expected)
def test_rabin_karp(test_input, expected):
    assert rabin_karp_search(*test_input) == expected
