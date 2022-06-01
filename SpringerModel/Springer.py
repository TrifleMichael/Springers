from enum import Enum
from math import pi, sin

from Utility.Point import Point
from Utility.Settings import GRAVITY_ACCELERATION, COLLISION_EPSILON, FLOOR_HEIGHT, RES_Y
from Utility.EuclidianFunctions import rotatePointAroundPoint, threePointAngle


class WeighBallState(Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3


class Springer:
    def __init__(self, head, foot, floorHeight):
        self.controllable = False
        self.head = head
        self.foot = foot

        self.footLanded = False
        self.headLanded = False
        self.weightBallState = WeighBallState.RIGHT

        self.floorHeight = floorHeight
        self.weightBallLength = 0.3  # given as percentage of whole length
        self.weighBallAngle = 3.1415 / 4

    def reactToCommands(self, newWeighBallState, ifBounce):
        self.weightBallState = newWeighBallState

    def calculateCenterMass(self, points):
        #  Assumes all points have the same mass
        x = 0
        y = 0
        for point in points:
            x += point.x
            y += point.y
        x /= len(points)
        y /= len(points)
        return Point(x, y)

    def getBallPosition(self):
        middleBallPosition = self.foot + (self.head - self.foot) * (1 - self.weightBallLength)
        if self.weightBallState == WeighBallState.LEFT:
            return rotatePointAroundPoint(middleBallPosition, self.head, self.weighBallAngle)
        if self.weightBallState == WeighBallState.MIDDLE:
            return middleBallPosition
        if self.weightBallState == WeighBallState.RIGHT:
            return rotatePointAroundPoint(middleBallPosition, self.head, -self.weighBallAngle)

    def move(self):
        self.checkGround()
        if self.footLanded and not self.headLanded:
            self.head.vy += GRAVITY_ACCELERATION
            self.moveHeadAroundFoot()
        if not self.footLanded and self.headLanded:
            self.foot.vy += GRAVITY_ACCELERATION
            self.moveFootAroundHead()
        if not self.footLanded and not self.headLanded:
            self.foot.vy += GRAVITY_ACCELERATION
            self.head.vy += GRAVITY_ACCELERATION
            self.foot.move()
            self.head.move()

    def checkGround(self):
        if abs(self.foot.y - (RES_Y - FLOOR_HEIGHT)) <= COLLISION_EPSILON:
            self.footLanded = True
            self.foot.vy = 0
            self.foot.vx = 0
            self.transferHeadMomentumWhenFootLands()

        if abs(self.head.y - (RES_Y - FLOOR_HEIGHT)) <= COLLISION_EPSILON:
            self.headLanded = True
            self.head.vy = 0
            self.head.vx = 0
            self.transferFootMomentumWhenHeadLands()

    def moveHeadAroundFoot(self):
        alpha = threePointAngle(self.head + self.head.getSpeedVector(), self.foot, self.head)
        newHead = rotatePointAroundPoint(self.head, self.foot, alpha)
        self.head.x = newHead.x
        self.head.y = newHead.y

    def transferHeadMomentumWhenFootLands(self):
        alpha = threePointAngle(self.head.getSpeedVector(), Point(0, 0), (self.foot - self.head).getNormalVector())
        newSpeedVector = rotatePointAroundPoint((self.foot - self.head).getNormalVector(), Point(0, 0), pi / 2)
        newSpeedVector = newSpeedVector.changeLength(abs(self.head.getSpeedVector()) * sin(alpha))
        self.head.vx = newSpeedVector.x
        self.head.vy = newSpeedVector.y

    def moveFootAroundHead(self):
        alpha = threePointAngle(self.foot + self.foot.getSpeedVector(), self.head, self.foot)
        newFoot = rotatePointAroundPoint(self.foot, self.head, alpha)
        self.foot.x = newFoot.x
        self.foot.y = newFoot.y

    def transferFootMomentumWhenHeadLands(self):
        alpha = threePointAngle(self.foot.getSpeedVector(), Point(0, 0), (self.head - self.foot).getNormalVector())
        newSpeedVector = rotatePointAroundPoint((self.head - self.foot).getNormalVector(), Point(0, 0), pi / 2)
        newSpeedVector = newSpeedVector.changeLength(abs(self.foot.getSpeedVector()) * sin(alpha))
        self.foot.vx = newSpeedVector.x
        self.foot.vy = newSpeedVector.y