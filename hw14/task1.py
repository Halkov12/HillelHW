# 1
# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()

# 2
# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string_ if char not in vowels)