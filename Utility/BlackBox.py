from SpringerModel.Springer import SpringState, WeighBallState
from Utility.EuclidianFunctions import threePointAngle
from Utility.Point import Point
from Utility.Settings import FLOOR_HEIGHT, TIME_LIMIT, STARTING_HEAD, START_FOOT


class BlackBox:
    def __init__(self, springerManager, levelManager):
        self.springerManager = springerManager
        self.levelManager = levelManager

    def changeSpringerStates(self):
        for springer in self.springerManager.springerList:
            info = self.getSpringerInfo(springer)
            genome = springer.genome

            # TODO: Na podstawie info (informacje o tym obiekcie sa na dole tego pliku) oraz genomu trzeba
            # TODO: wybrac WeighBallState oraz SpringState do wrzucenia w ponizsza linie
            # TODO: WeighBallState i SpringState to enumy. Sa opisane u gory Springers.py

            # TODO: Genom moze byc dowolnie zmieniony, nie wykorzystuje go nigdzie indziej.
            # TODO: Czyli po prostu trzeba zrobic funkcje, ktora na podstawie genomu i aktualnej sytuacji podejmuje decyzje danego springera :)

            self.giveSpringerInstructions(springer, WeighBallState.LEFT, SpringState.EXTENDED)

    def iterate(self):
        self.changeSpringerStates()
        if self.levelManager.timeFromStart >= TIME_LIMIT:
            self.generateNewGeneration()
            self.levelManager.timeFromStart = 0

    def generateNewGeneration(self):
        newGenomes = []
        for springer1 in self.springerManager.springerList:
            for springer2 in self.springerManager.springerList:
                pass
                # TODO: Dodawac nowe genomy na podstawie genomow powyzszych Springerow (springer1.genome i springer2.genome)
                # TODO: Jako metryka dopasowania starego genotypu moze przydac sie getSpringerSuccessMetric(), aktualnie to po prostu kwadrat odleglosci przebytej
                # TODO: Ta funkcja uruchamia sie regularnie co TIME_LIMIT (zdefiniowany w Settings, aktualnie ok 5 sekund).

        self.deleteOldSpringers()
        for genome in newGenomes:
            self.levelManager.addControllableSpringer(STARTING_HEAD, START_FOOT, genome)
        print("RECOMBINING GENOMES")

    def getSpringerSuccessMetric(self, springer):
        return springer.head.x ** 2

    def deleteOldSpringers(self):
        self.springerManager.springerList = []
        self.levelManager.drawManager.springerSpriteList = []

    def giveSpringerInstructions(self, springer, ballState, springState):
        springer.changeBallState(ballState)
        if springState == SpringState.EXTENDED:
            springer.extendSpring()
        elif springState == SpringState.RETRACTED:
            springer.shortenSpring()
        springer.move()

    def getSpringerInfo(self, springer):
        angle = threePointAngle(springer.foot + Point(0, 1), springer.foot, springer.head)
        height = springer.foot.y - FLOOR_HEIGHT
        timeFromStart = self.levelManager.timeFromStart
        return SpringerInfo(angle, height, timeFromStart)


class SpringerInfo:
    def __init__(self, angle, height, timeFromStart):
        self.angle = angle  # Angle from graphical DOWN direction to head of springer. Counted counterclockwise.
        self.height = height  # Distance of foot from floor. Can be negative if foot sinks into the ground.
        self.timeFromStart = timeFromStart  # Frames since the simulation began
