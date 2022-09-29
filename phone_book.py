class PhoneBook:
    def __init__(self):
        self._phones_to_names = {}
        self._names_to_phones = {}

    def add_contact(self, name, phone_number):
        self._names_to_phones[name] = phone_number
        self._phones_to_names[phone_number] = name

    def delete_contact(self, name=None, phone_number=None):
        assert not (name and phone_number), 'Either `name` or `phone_number` must be provided. Not both!'

        if name is not None:
            if name in self._names_to_phones:
                del self._phones_to_names[self._names_to_phones[name]]
                del self._names_to_phones[name]

        if phone_number is not None:
            if phone_number in self._phones_to_names:
                del self._names_to_phones[self._phones_to_names[phone_number]]
                del self._phones_to_names[phone_number]

    def find(self, name=None, phone_number=None):
        assert not (name and phone_number), 'Either `name` or `phone_number` must be provided. Not both!'

        if name is not None:
            return self._names_to_phones.get(name, 'not found')

        if phone_number is not None:
            return self._phones_to_names.get(phone_number, 'not found')
