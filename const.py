import colorama
from colorama import Fore, Back, Style

FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

SIZE = (30, 105)

MIN_MUTATION_PRICE = 25

MUTATION_PRICES = [["speed", [0, 25, 30]], ["spaciousness", [0, 25, 30]], [ "strength", [0, 35, 50]]]

FOOD_TYPES = [{"name": "meat", "power": 50}, {"name": "green", "power":  20}, {"name": "fertilizer", "power": 35}, {"name": "dangerous", "power": -50}]
ENTOURAGE_TYPES = [{"name": "grass"}]

CREATION_COLORS = [ Fore.BLACK, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
