from SpringerModel.Springer import WeighBallState, SpringState


class SpringerManager:
    def __init__(self):
        self.springerList = []

        self.newWeighBallState = WeighBallState.DEFAULT
        self.springState = SpringState.DEFAULT

    def addSpringer(self, springer):
        self.springerList.append(springer)

    def moveSpringers(self):
        for springer in self.springerList:
            if springer.controllable:
                if self.newWeighBallState != WeighBallState.DEFAULT:
                    springer.changeBallState(self.newWeighBallState)
                if self.springState == SpringState.EXTENDED:
                    springer.extendSpring()
                elif self.springState == SpringState.RETRACTED:
                    springer.shortenSpring()
            springer.move()

    def changeBallState(self, newWeighBallState):
        self.newWeighBallState = newWeighBallState

