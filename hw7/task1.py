from decimal import Decimal

class frange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = Decimal(0)
            self.end = Decimal(args[0])
            self.step = Decimal(1)
        elif len(args) == 2:
            self.start = Decimal(args[0])
            self.end = Decimal(args[1])
            self.step = Decimal(1)
        elif len(args) == 3:
            self.start = Decimal(args[0])
            self.end = Decimal(args[1])
            self.step = Decimal(args[2])

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.end) or (self.step < 0 and self.current <= self.end):
            raise StopIteration

        result = float(self.current)
        self.current += self.step
        return result



assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')