from Managers.DrawManager import DrawManager
from Utility.Settings import FLOOR_HEIGHT, HEADLESS_MODE
from SpringerModel.Springer import Springer
from Managers.SpringerManager import SpringerManager
from SpringerModel.SpringerSprite import SpringerSprite


class LevelManager:
    def __init__(self, display):
        self.display = display
        self.springerManager = SpringerManager()
        self.drawManager = DrawManager(display)
        self.timeFromStart = 0

    def draw(self):
        self.drawManager.draw()

    def iterate(self):
        self.springerManager.moveSpringers()
        self.timeFromStart += 1

    def addSpringer(self, head, foot):
        springer = Springer(head, foot, FLOOR_HEIGHT)
        springerSprite = SpringerSprite(springer, self.display)

        self.drawManager.addSpringerSprite(springerSprite)
        self.springerManager.addSpringer(springer)

    def addControllableSpringer(self, head, foot, genome):
        springer = Springer(head, foot, FLOOR_HEIGHT)
        springer.genome = genome
        springer.controllable = True
        springerSprite = SpringerSprite(springer, self.display)

        self.drawManager.addSpringerSprite(springerSprite)
        self.springerManager.addSpringer(springer)

    def updateDisplay(self, display):
        self.display = display
        self.drawManager.updateDisplay(display)
