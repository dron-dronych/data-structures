from parentheses_check import find_broken_bracket


def test_find_broken_brackets():
    test_statements = {
        '([{}])': 0,
        '([{{])': 1
    }

    for stmt in test_statements:
        assert find_broken_bracket(stmt) == test_statements[stmt]

