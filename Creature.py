import colorama, random, time, copy

from Food import Food
from const import *
from colorama import Fore, Back, Style

colorama.init()

pos = lambda x, y: '\x1b[%d;%dH' % (x, y)

class Creature:
    def __init__(self, x, y, mutation = {}):
        self.x = x
        self.y = y
        self.age = 0
        self.hunger = 100
        self.health = 100

        self.speed = 1
        self.spaciousness = 1
        self.strength = 1

        self.color = Fore.YELLOW

        if (mutation != {}): self.isMutant = True

        try:
            self.speed = mutation["speed"]
        except:
            pass
        try:
            self.spaciousness = mutation["spaciousness"]
        except:
            pass
        try:
            self.strength = mutation["strength"]
        except:
            pass
        try:
            self.color = mutation["color"]
        except:
            pass
        
        self.mutation = {}
        self.inherited_mutation = mutation

    def concat_mutations(self):
        if (len(self.inherited_mutation) == 0): return False
        mutation_copy = copy.copy(self.inherited_mutation)

        for i in mutation_copy:
            if i in self.mutation:
                mutation_copy[i] = self.mutation[i]
        
        self.mutation = mutation_copy

        return True

    def Multiply(self, world):
        directionX = random.randint(-5, 5)
        while self.x + directionX > SIZE[0] - 1 or self.x + directionX < 1:
            directionX = random.randint(-5, 5)
        directionY = random.randint(-5, 5)
        while self.y + directionY > SIZE[1] - 1 or self.y + directionY < 1:
            directionY = random.randint(-5, 5)
        

        if (len(self.inherited_mutation) > 0 and len(self.mutation) == 0):
            self.mutation = self.inherited_mutation

        world[self.x + directionX][self.y + directionY].append(Creature(self.x + directionX, self.y + directionY, self.mutation))

        self.mutation = {}

        return [world, [self.x + directionX, self.y + directionY]]

    def GenerateMutation(self):
        score = 50

        while True:
            if (score < MIN_MUTATION_PRICE): break
            choice = random.choice(MUTATION_PRICES)
            while choice[1][1] > score:
                choice = random.choice(MUTATION_PRICES)
            
            # price = random.choice(choice[1])
            # print(choice[1])
            priceIndex = random.randint(1, len(choice[1]) - 1)
            price = choice[1][priceIndex]
            while price > score:
                priceIndex = random.randint(1, len(choice[1]) - 1)
                price = choice[1][priceIndex]
            
            score -= price
            self.mutation[choice[0]] = priceIndex + 1
        
        self.mutation["color"] = random.choice(CREATION_COLORS)
        
        self.concat_mutations()

    def MakeStep(self, world):
        log = []

        if (self.health <= 0):
            log.append(["death"])
            return [world, log]

        if (self.age > 10):
            stepNum = random.randint(0, 15)
        else:
            stepNum = random.randint(0, 10)

        eatResult = self.Eat(world)
        world = eatResult[0]

        log.append(["eat", [self.x, self.y, eatResult[1]]])
        
        if (self.health <= 0):
            log.append(["death"])
            return [world, log]

        if (eatResult[1] == -1):
            self.hunger -= 10 * 1 / self.strength
        if (stepNum < 10):
            self.Go()
            log.append(["go", [self.x, self.y]])
        elif (stepNum > 10):
            if (random.randint(0, 5) == 0): self.GenerateMutation()
            multiplyResult = self.Multiply(world)
            world = multiplyResult[0]
            log.append(["multiply", multiplyResult[1]])

        self.age += 1

        if (self.age >= 30):
            if (random.randint(0, 3) == 0):
                self.health = 0
        elif (self.hunger <= 0):
            self.health = 0

        return [world, log]
    
    def Eat(self, world):
        index = -1
        for element in world[self.x][self.y]:
            if (isinstance(element, Food)):
                if (self.hunger + element.getType()["power"] * self.spaciousness <= 100):
                    self.hunger += element.getType()["power"] * self.spaciousness
                else:
                    self.hunger = 100
                world[self.x][self.y].remove(element)
                index = 0
        return [world, index]
            
    def Die(self):
        self.health = 0
        self.Print()

    def Go(self):
        for i in range(self.speed):
            gx = random.randint(-1, 1)
            while self.x + gx > SIZE[0] - 1 or self.x + gx < 1:
                gx = random.randint(-1, 1)
            gy = random.randint(-1, 1)
            while self.y + gy > SIZE[1] - 1 or self.y + gy < 1:
                gy = random.randint(-1, 1)

            self.x += gx
            self.y += gy

            print('%s%s%s%s%s' % (pos(self.x - gx + 1, self.y - gy + 1), Fore.GREEN, Back.BLACK, Style.BRIGHT, ","), end='')
    

    def Print(self):
        pos = lambda x, y: '\x1b[%d;%dH' % (x, y)

        if (self.age >= 0 and self.age < 10):
            print('%s%s%s%s%s' % (pos(self.x + 1, self.y + 1), self.color, Back.BLACK, Style.BRIGHT, "h"), end='')
        elif (self.age >= 10 and self.age < 20):
            print('%s%s%s%s%s' % (pos(self.x + 1, self.y + 1), self.color, Back.BLACK, Style.BRIGHT, "H"), end='')
        elif (self.age >= 20 and self.age < 30):
            print('%s%s%s%s%s' % (pos(self.x + 1, self.y + 1), self.color, Back.BLACK, Style.BRIGHT, "I"), end='')
        
        if (self.health <= 0):
            print('%s%s%s%s%s' % (pos(self.x + 1, self.y + 1), self.color, Back.BLACK, Style.BRIGHT, "*"), end='')