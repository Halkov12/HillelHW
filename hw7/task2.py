from colorama import Fore, init

init(autoreset=True)


class colorizer:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color == 'red':
            self.color_code = Fore.RED
        elif self.color == 'green':
            self.color_code = Fore.GREEN
        elif self.color == 'blue':
            self.color_code = Fore.BLUE
        else:
            self.color_code = Fore.WHITE
        return self.color_code

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with colorizer('red') as c:
    print(f'{c}printed in red')

with colorizer('green') as c:
    print(f'{c}printed in green')

with colorizer('blue') as c:
    print(f'{c}printed in blue')


print('printed in default')