from network import process_packets
import pytest


expected = [
    ('1, 1, [(0, 0)]', [0]),
    ('1, 2, [(0, 1), (0, 1)]', [0, -1]),
    ('1, 2, [(0, 1), (1, 1)]', [0, 1])
]


@pytest.mark.parametrize('test_input, expected', expected)
def test_process_packets(test_input, expected):
    assert process_packets(*eval(test_input)) == expected