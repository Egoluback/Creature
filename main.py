import colorama, random, time

from colorama import Fore, Back, Style
from Creation import Creation
from const import *
from Food import Food

FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

colorama.init()

world = []

creationsIndexes = []
foodIndexes = []

pos = lambda x, y: '\x1b[%d;%dH' % (x, y)

creationsCount = 10

def createWorld():
    for i in range(SIZE[0]):
        toAddY = []
        for j in range(SIZE[1]):
            toAdd = []

            if (random.randint(0, 5) == 0):
                foodIndexes.append([i, j])
                toAdd.append(Food(random.choice(FOOD_TYPES)))

            toAddY.append(toAdd)
        world.append(toAddY)
    
    for creationIndex in range(creationsCount):
        posX = random.randint(0, SIZE[0] - 1)
        posY = random.randint(0, SIZE[1] - 1)
        
        creation = Creation(posX, posY)
        world[posX][posY].append(creation)
        
        creationsIndexes.append([posX, posY])
    
    # print(len(world), len(world[0]))
    # input()

def printObjects():
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            if (len(world[i][j]) != 0):
                # for element in world[i][j]:
                element = world[i][j][len(world[i][j]) - 1]
                if (isinstance(element, Creation)):
                    element.Print()
                elif (isinstance(element, Food)):
                    # for foodIndex in foodIndexes:
                    #     for element in world[foodIndex[0]][foodIndex[1]]:
                    #         if (isinstance(element, Food)):
                    element.Print([i, j])
                    # print('%s%s%s%s%s' % (pos(i + 1, j + 1), Fore.GREEN, Back.BLACK, Style.BRIGHT, "$"), end='')

def printWorld():
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            print('%s%s%s%s%s' % (pos(i + 1, j + 1), Fore.GREEN, Back.BLACK, Style.BRIGHT, ","), end='')
    
    printObjects()
            

def clearFullScreen():
	for i in range(1, 30):
		for j in range(1, 80):
			print('%s%s%s%s%s' % (pos(i + 1, j + 1), Fore.BLACK, Back.BLACK, Style.BRIGHT, " "), end='')

pos = lambda x, y: '\x1b[%d;%dH' % (x, y)
# print('%s%s%s%s%s' % (pos(10,20), Fore.BLACK, Back.BLACK, Style.BRIGHT,"Ресурсов:"), end='')
# otv = int(input(""))
# print('%s%s%s%s%s' % (pos(12,20), Fore.BLACK, Back.BLACK, Style.BRIGHT,"Существ изначально:"), end='')
# creationCount = int(input(""))
clearFullScreen()
# creation.verr = otv

createWorld()
printWorld()

# for i in range(0,otv2):
# 	hu = creation(random.randint(1,20),random.randint(1,69),0)
# 	creations.append(hu)

iterationCount = 0

while True:
    for creationIndex in creationsIndexes:
        # input()
        # try:
        for element in world[creationIndex[0]][creationIndex[1]]:
            if (isinstance(element, Creation)):
                step = element.MakeStep(world)
                world = step[0]
                log = step[1]
                for logEl in log:
                    if (logEl[0] == "death"):
                        element.Print()
                        world[creationIndex[0]][creationIndex[1]].remove(element)
                        creationsIndexes.remove(creationIndex)
                        del element
                        world[creationIndex[0]][creationIndex[1]].append(Food(FOOD_TYPES[2]))
                        continue
                    elif (logEl[0] == "multiply"):
                        creationsIndexes.append(logEl[1])
                
        # except:
        #     print(world[creationIndex[0]][creationIndex[1]])
        #     print('%s%s%s%s%s' % (pos(20, 80), Fore.YELLOW, Back.BLACK, Style.BRIGHT, creationIndex[2]), end='')
        #     input()

    if (len(creationsIndexes) >= 120):
        for creationIndex in creationsIndexes:
            for element in world[creationIndex[0]][creationIndex[1]]:
                if (isinstance(element, Creation)):
                    if (random.randint(0, 99) <= 98):
                        element.Die()
                        world[creationIndex[0]][creationIndex[1]].remove(element)
                        creationsIndexes.remove(creationIndex)
                        del element
                        world[creationIndex[0]][creationIndex[1]].append(Food(FOOD_TYPES[2]))
                        continue


    printObjects()
    # printcreations()
    time.sleep(0.2)
    iterationCount += 1
    
    print('%s%s%s%s%s' % (pos(15, 110), Fore.YELLOW, Back.BLACK, Style.BRIGHT, len(creationsIndexes)), end='')
    print('%s%s%s%s%s' % (pos(20, 110), Fore.YELLOW, Back.BLACK, Style.BRIGHT, iterationCount), end='')