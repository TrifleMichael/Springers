from Utility.Point import Point
from Utility.Settings import START_FOOT_COORDS, START_HEAD_COORDS
from random import randrange, randint


def getStartFoot():
    return Point(START_FOOT_COORDS[0], START_FOOT_COORDS[1])


def getStartHead():
    return Point(START_HEAD_COORDS[0], START_HEAD_COORDS[1])

def getRandomGenome():
    genome = [[] for _ in range(10)]
    for row in genome:
        for _ in range(8):
            a = randint(0, 10)
            b = randint(0, 10)
            c = randint(0, 10-b)
            row.append((b, c, 10-b-c, a, 10-a))
    return genome

def createRandomGenomeSpringers(n, levelManager):
    for i in range(n):
        levelManager.addControllableSpringer(getStartHead(), getStartFoot(), getRandomGenome())
