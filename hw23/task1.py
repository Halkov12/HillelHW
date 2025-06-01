def custom_map(dictionary, func1, func2):
    new_dict = {}
    for key, value in dictionary.items():
        new_key = func1(key)
        new_value = func2(value)
        new_dict[new_key] = new_value
    return new_dict

my_dictionary = {'a': 1, 'b': 2, 'c': 3}

def func_1(key):
    return key + key

def func_2(value):
    return value**2

print(custom_map(my_dictionary, func_1, func_2))