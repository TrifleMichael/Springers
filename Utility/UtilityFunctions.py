from Utility.Point import Point
from Utility.Settings import START_FOOT_COORDS, START_HEAD_COORDS
from random import randrange


def getStartFoot():
    return Point(START_FOOT_COORDS[0], START_FOOT_COORDS[1])


def getStartHead():
    return Point(START_HEAD_COORDS[0], START_HEAD_COORDS[1])

def getRandomGenome():
    return [[randrange(10) for _ in range(5)] for _ in range(8)]

def createRandomGenomeSpringers(n, levelManager):
    for i in range(n):
        levelManager.addControllableSpringer(getStartHead(), getStartFoot(), getRandomGenome())
