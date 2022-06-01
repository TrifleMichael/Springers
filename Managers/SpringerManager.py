from SpringerModel.Springer import WeighBallState


class SpringerManager:
    def __init__(self):
        self.springerList = []

        self.newWeighBallState = WeighBallState.RIGHT
        self.ifBounce = False


    def addSpringer(self, springer):
        self.springerList.append(springer)

    def moveSpringers(self):
        for springer in self.springerList:
            if springer.controllable:
                springer.reactToCommands(self.newWeighBallState, self.ifBounce)
            springer.move()

    def updateControlls(self, newWeighBallState, ifBounce):
        self.newWeighBallState = newWeighBallState
        self.ifBounce = ifBounce
