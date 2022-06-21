from Utility.Point import Point
from Utility.Settings import START_FOOT_COORDS, START_HEAD_COORDS


def getStartFoot():
    return Point(START_FOOT_COORDS[0], START_FOOT_COORDS[1])


def getStartHead():
    return Point(START_HEAD_COORDS[0], START_HEAD_COORDS[1])