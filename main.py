import colorama, random, time

from colorama import Fore, Back, Style

from World import World
from Creature import Creature
from Food import Food
from const import *

colorama.init()

world = []

pos = lambda x, y: '\x1b[%d;%dH' % (x, y)

world = World(10, [0, 1])

world.Create()
world.Print()

iterationCount = 0

while True:
    toPrintObj = []
    world_session = world.get_World()
    creaturesIndexes_session = world.get_CreaturesIndexes()
    foodIndexes_session = world.get_FoodIndexes()
    for creationIndex in world.get_CreaturesIndexes():
        for element in world_session[creationIndex[0]][creationIndex[1]]:
            if (isinstance(element, Creature)):
                step = element.MakeStep(world_session)
                world_session = step[0]
                log = step[1]
                for logEl in log:
                    if (logEl[0] == "death"):
                        element.Print()
                        world_session[creationIndex[0]][creationIndex[1]].remove(element)
                        creaturesIndexes_session.remove(creationIndex)
                        del element
                        world_session[creationIndex[0]][creationIndex[1]].append(Food(FOOD_TYPES[2]))
                        continue
                    elif (logEl[0] == "multiply"):
                        creaturesIndexes_session.append(logEl[1])
                    elif (logEl[0] == "eat"):
                        toPrintObj.append(logEl[1])
                    elif (logEl[0] == "go"):
                        toPrintObj.append(logEl[1])
                
    if (len(creaturesIndexes_session) >= 700):
        for creationIndex in creaturesIndexes_session:
            for element in world_session[creationIndex[0]][creationIndex[1]]:
                if (isinstance(element, Creature)):
                    if (random.randint(0, 99) <= 98):
                        element.Die()
                        world_session[creationIndex[0]][creationIndex[1]].remove(element)
                        creaturesIndexes_session.remove(creationIndex)
                        del element
                        world_session[creationIndex[0]][creationIndex[1]].append(Food(FOOD_TYPES[2]))
                        continue


    world.PrintObjects(toPrintObj)

    world.set_World(world_session)
    world.set_CreaturesIndexes(creaturesIndexes_session)
    world.set_FoodIndexes(foodIndexes_session)

    time.sleep(0.2)
    iterationCount += 1
    
    print('%s%s%s%s%s' % (pos(15, 110), Fore.YELLOW, Back.BLACK, Style.BRIGHT, len(creaturesIndexes_session)), end='')
    print('%s%s%s%s%s' % (pos(20, 110), Fore.YELLOW, Back.BLACK, Style.BRIGHT, iterationCount), end='')

