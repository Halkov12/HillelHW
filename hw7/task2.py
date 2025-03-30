from colorama import Fore, init

class Colorizer:
    COLORS = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'blue': Fore.BLUE,
        'yellow': Fore.YELLOW,
        'cyan': Fore.CYAN,
        'magenta': Fore.MAGENTA,
        'white': Fore.WHITE
    }

    def __init__(self, color):
        self.color_code = self.COLORS.get(color, Fore.WHITE)

    def __enter__(self):
        print(self.color_code, end="")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(Fore.RESET, end="")


with Colorizer('red'):
    print("Printed in red")

with Colorizer('green'):
    print("Printed in green")

with Colorizer('blue'):
    print("Printed in blue")

with Colorizer('yellow'):
    print("Printed in yellow")

with Colorizer('cyan'):
    print("Printed in cyan")

with Colorizer('magenta'):
    print("Printed in magenta")

print("Printed in default")