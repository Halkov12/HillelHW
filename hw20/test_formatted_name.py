import unittest

def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

class TestFormattedName(unittest.TestCase):
    def test_first_last_name(self):
        result = formatted_name('firstname', 'lastname')
        self.assertEqual(result, 'Firstname Lastname')

    def test_full_name_with_middle(self):
        result = formatted_name('firstname', 'lastname', 'middlename')
        self.assertEqual(result, 'Firstname Middlename Lastname')

    def test_empty_middle_name(self):
        result = formatted_name('firstname', 'lastname', '')
        self.assertEqual(result, 'Firstname Lastname')

    def test_uppercase_input(self):
        result = formatted_name('FIRSTNAME', 'LASTNAME', 'MIDDLENAME')
        self.assertEqual(result, 'Firstname Middlename Lastname')

    def test_empty_values(self):
        result = formatted_name('', '')
        self.assertEqual(result, '')

        result = formatted_name('', 'lastname')
        self.assertEqual(result, 'Lastname')

        result = formatted_name('firstname', '')
        self.assertEqual(result, 'Firstname')

        result = formatted_name('', 'lastname', '')
        self.assertEqual(result, 'Lastname')
