from math import *

from Utility.Point import Point


def rotatePointAroundPoint(rotated, center, angle):
    """Rotates point clockwise around center point"""
    temp = rotated - center
    temp = Point(temp.x * cos(angle) - temp.y * sin(angle),
                 temp.x * sin(angle) + temp.y * cos(angle))
    return temp + center


def lineAngle(p1, p2):
    """Angle in relation to up direction, counted clockwise"""
    return -(atan2(p2.x - p1.x, p2.y - p1.y) - pi) % (2 * pi)


def threePointAngle(p1, p2, p3):
    """Angle at point p2, counted from p3 to p1"""
    return lineAngle(p2, p1) - lineAngle(p2, p3)
