import pytest
from phone_book import PhoneBook


phone_book = PhoneBook()


@pytest.mark.parametrize(
    'test_input, expected',
    [
        ('add 911 police', None),
        ('add 76213 Mom', None),
        ('add 17239 Bob', None),
        ('find 76213', 'Mom'),
        ('find 910', 'not found'),
        ('find 911', 'police'),
        ('del 910', None),
        ('del 911', None),
        ('find 911', 'not found'),
        ('find 76213', 'Mom'),
        ('add 76213 daddy', None),
        ('find 76213', 'daddy'),
    ]
)
def test_phone_book(test_input, expected):
    command, *args = test_input.split(' ')

    if len(args) == 2:
        phone_number, name = args
    elif len(args) == 1:
        phone_number = args[0]

    if command == 'add':
        res = phone_book.add_contact(name, phone_number)

    elif command == 'find':
        res = phone_book.find(phone_number=phone_number)

    elif command == 'del':
        res = phone_book.delete_contact(phone_number=phone_number)

    else:
        raise ValueError(f'unknown command `{command}`')

    assert res == expected
