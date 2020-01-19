import colorama, random, time

from const import *
from colorama import Fore, Back, Style

colorama.init()

pos = lambda x, y: '\x1b[%d;%dH' % (x, y)

class Food:
    def __init__(self, type):
        self.type = type
    
    def Print(self, position):
        if (self.type["name"] == "fertilizer"):
            print('%s%s%s%s%s' % (pos(position[0] + 1, position[1] + 1), Fore.BLACK, Back.BLACK, Style.BRIGHT, "*"), end='')
        elif (self.type["name"] == "dangerous"):
            print('%s%s%s%s%s' % (pos(position[0] + 1, position[1] + 1), Fore.RED, Back.BLACK, Style.BRIGHT, "$"), end='')
        else:
            print('%s%s%s%s%s' % (pos(position[0] + 1, position[1] + 1), Fore.GREEN, Back.BLACK, Style.BRIGHT, "$"), end='')
    
    def getType(self):
        return self.type