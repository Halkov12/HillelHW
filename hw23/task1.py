class CustomMap:
    def __init__(self, dictionary: dict, func1, func2):
        self._items = list(dictionary.items())
        self.func1 = func1
        self.func2 = func2
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self._items):
            raise StopIteration

        key, value = self._items[self.index]
        self.index += 1
        return self.func1(key), self.func2(value)


my_dictionary = {'a': 1, 'b': 2, 'c': 3}

def func_1(key):
    return key + key

def func_2(value):
    return value**2

for i, j in CustomMap(my_dictionary, func_1, func_2):
    print(i, j)