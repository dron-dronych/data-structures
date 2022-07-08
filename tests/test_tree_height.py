import pytest
from tree_height import Tree


expected = [
    ('Tree(5, [4, -1, 4, 1, 1])', 3),
    ('Tree(5, [-1, 0, 4, 0, 3])', 4),
]


@pytest.mark.parametrize('test_input, expected', expected)
def test_tree_height(test_input, expected):
    assert eval(test_input).height == expected