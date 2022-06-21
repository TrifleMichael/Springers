from SpringerModel.Springer import SpringState, WeighBallState
from Utility.EuclidianFunctions import threePointAngle
from Utility.Point import Point
from Utility.Settings import FLOOR_HEIGHT, TIME_LIMIT, MUTATION_CHANCE
import random as rd
import copy

from Utility.UtilityFunctions import getStartHead, getStartFoot


class BlackBox:
    def __init__(self, springerManager, levelManager):
        self.springerManager = springerManager
        self.levelManager = levelManager
        self.generationNumber = 1

        self.bestGenerationGenomes = None
        self.bestGenerationMetric = None

    def changeSpringerStates(self):
        for springer in self.springerManager.springerList:
            info = self.getSpringerInfo(springer)
            genome = springer.genome
            angleReactionIndex = int(info.angle / 6.28 * 1000 // 125)
            a, s, d, q, e = genome[angleReactionIndex]
            tempList = []
            state = {a: WeighBallState.LEFT, s: WeighBallState.MIDDLE, d: WeighBallState.RIGHT}
            for w in (a, s, d):
                for _ in range(int(w)):
                    tempList.append(state[w])
            weighBallState = tempList[rd.randint(0, len(tempList) - 1)]
            if q < rd.random() * 10:
                springState = SpringState.RETRACTED
            else:
                springState = SpringState.EXTENDED
            self.giveSpringerInstructions(springer, weighBallState, springState)

    def iterate(self):
        self.changeSpringerStates()
        if self.levelManager.timeFromStart >= TIME_LIMIT:
            self.generateNewGeneration()
            self.levelManager.timeFromStart = 0

    def generateNewGeneration(self):
        newGenomes = []
        oldGenomes = []
        self.springerManager.springerList.sort(key=self.getSpringerSuccessMetric)
        n = len(self.springerManager.springerList)
        for springer1 in self.springerManager.springerList[n // 2:]:
            for springer2 in self.springerManager.springerList[n // 2:]:
                currGenome = self.combineGenomes(springer1.genome, springer2.genome)
                currGenome = self.mutate(currGenome)
                newGenomes.append(currGenome)
            oldGenomes.append(springer1.genome)

        self.printGenerationInfo()
        self.saveIfBestGeneration(oldGenomes, self.getSpringerSuccessMetric(self.springerManager.springerList[0]))
        self.deleteOldSpringers()
        for genome in newGenomes:
            self.levelManager.addControllableSpringer(getStartHead(), getStartFoot(), genome)
        self.generationNumber += 1

    def combineGenomes(self, genome1, genome2):
        genome = [tuple([(genome1[i][j] + genome2[i][j]) / 2 for j in range(len(genome1[i]))]) for i in
                  range(len(genome1))]
        return genome

    def mutate(self, genome):
        for i in range(len(genome)):
            mutatedGene = list(genome[i])
            oldGene = list(genome[i])
            if rd.uniform(0, 1) <= MUTATION_CHANCE:
                mutationType = rd.choice([0,1])
                if mutationType == 0:
                    from_to = rd.sample([0, 1, 2], k=2)
                    mutatedGene[from_to[0]], mutatedGene[from_to[1]] = mutatedGene[from_to[1]], mutatedGene[from_to[0]]
                else:
                    mutatedGene[3], mutatedGene[4] = mutatedGene[4], mutatedGene[3]
            genome[i] = tuple(mutatedGene)

        return genome

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

    def printGenerationInfo(self):
        averageSuccess = 0
        bestSuccess = 0
        for springer in self.springerManager.springerList:
            averageSuccess += self.getSpringerSuccessMetric(springer)
            bestSuccess = max(bestSuccess, self.getSpringerSuccessMetric(springer))
        averageSuccess /= len(self.springerManager.springerList)

        print("----------------------------------")
        print("Generation ", self.generationNumber)
        print("Average success metric: ", int(averageSuccess))
        print("Best success metric: ", int(bestSuccess))

    def saveIfBestGeneration(self, genomes, metric):
        if self.bestGenerationGenomes is not None:
            if metric > self.bestGenerationMetric:
                self.bestGenerationGenomes = copy.deepcopy(genomes)
                self.bestGenerationMetric = metric
        else:
            self.bestGenerationGenomes = copy.deepcopy(genomes)
            self.bestGenerationMetric = metric

    def prepareReplay(self):
        self.deleteOldSpringers()
        for genome in self.bestGenerationGenomes:
            self.levelManager.addControllableSpringer(getStartHead(), getStartFoot(), genome)

class SpringerInfo:
    def __init__(self, angle, height, timeFromStart):
        self.angle = angle  # Angle from graphical DOWN direction to head of springer. Counted counterclockwise.
        self.height = height  # Distance of foot from floor. Can be negative if foot sinks into the ground.
        self.timeFromStart = timeFromStart  # Frames since the simulation began
