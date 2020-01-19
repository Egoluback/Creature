import colorama, random, time

from const import *
from Creature import Creature
from Food import Food
from colorama import Fore, Back, Style

FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

colorama.init()

pos = lambda x, y: '\x1b[%d;%dH' % (x, y)

class World:
    def __init__(self, creaturesCount, foodChance):
        self.creaturesCount = creaturesCount
        self.foodChance = foodChance  

        self.World = []

        self.CreaturesIndexes = []
        self.FoodIndexes = []

    def Create(self):
        for i in range(SIZE[0]):
            toAddY = []
            for j in range(SIZE[1]):
                toAdd = []

                if (random.randint(self.foodChance[0], self.foodChance[1]) == 0):
                    self.FoodIndexes.append([i, j])
                    toAdd.append(Food(random.choice(FOOD_TYPES)))

                toAddY.append(toAdd)
            self.World.append(toAddY)
        
        for creationIndex in range(self.creaturesCount):
            posX = random.randint(0, SIZE[0] - 1)
            posY = random.randint(0, SIZE[1] - 1)
            
            creation = Creature(posX, posY)
            self.World[posX][posY].append(creation)
            
            self.CreaturesIndexes.append([posX, posY])
    
    def PrintObjects(self):
        for i in range(SIZE[0]):
            for j in range(SIZE[1]):
                if (len(self.World[i][j]) != 0):
                    element = self.World[i][j][len(self.World[i][j]) - 1]
                    if (isinstance(element, Creature)):
                        element.Print()
                    elif (isinstance(element, Food)):
                        element.Print([i, j])
    
    def Print(self):
        for i in range(SIZE[0]):
            for j in range(SIZE[1]):
                print('%s%s%s%s%s' % (pos(i + 1, j + 1), Fore.GREEN, Back.BLACK, Style.BRIGHT, ","), end='')
        
        self.PrintObjects()
    
    def get_World(self):
        return self.World
    
    def get_CreaturesIndexes(self):
        return self.CreaturesIndexes
    
    def get_FoodIndexes(self):
        return self.FoodIndexes

    def set_World(self, new):
        self.World = new
    
    def set_CreaturesIndexes(self, new):
        self.CreaturesIndexes = new
    
    def set_FoodIndexes(self, new):
        self.FoodIndexes = new
