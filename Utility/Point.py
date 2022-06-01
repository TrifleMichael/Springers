from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def getTouple(self):
        return self.x, self.y

    def getSpeed(self):
        return sqrt(self.vx**2 + self.vy**2)

    def getSpeedVector(self):
        return Point(self.vx, self.vy)

    def getNormalVector(self):
        return Point(self.x / abs(self), self.y / abs(self))

    def getSpeedNormalVector(self):
        return Point(self.vx / self.getSpeed(), self.vy / self.getSpeed())

    def changeLength(self, length):
        return self.getNormalVector() * length

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Point(self.x * other, self.y * other)
        else:
            raise Exception("Wrong argument for multiplication given")

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"
