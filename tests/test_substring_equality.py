import pytest
from substring_equality import substring_equality


expected_res = [
    (('trololo', 2, 4, 3), 1),
    (('trololo', 3, 5, 1), 1),
    (('trololo', 0, 0, 7), 1),
    (('trololo', 1, 3, 2), 0),
]


@pytest.mark.parametrize('test_input, expected', expected_res)
def test_substring_equality(test_input, expected):
    assert substring_equality(*test_input) == expected
