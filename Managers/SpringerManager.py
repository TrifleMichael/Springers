from SpringerModel.Springer import WeighBallState


class SpringerManager:
    def __init__(self):
        self.springerList = []

        self.newWeighBallState = WeighBallState.RIGHT
        self.springExtended = True


    def addSpringer(self, springer):
        self.springerList.append(springer)

    def moveSpringers(self):
        for springer in self.springerList:
            if springer.controllable:
                springer.changeBallState(self.newWeighBallState)

                if self.springExtended:
                    springer.extendSpring()
                else:
                    springer.shortenSpring()

            springer.move()

    def changeBallState(self, newWeighBallState):
        self.newWeighBallState = newWeighBallState

    def changeSpringState(self, springExtended):
        self.springExtended = springExtended
