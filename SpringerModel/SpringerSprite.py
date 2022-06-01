import pygame.draw

from SpringerModel.Springer import WeighBallState


class SpringerSprite:
    def __init__(self, springerModel, display):
        self.springerModel = springerModel
        self.display = display
        self.color = (0, 0, 255)
        self.weightColor = (255, 0, 0)
        self.width = 5
        self.weightRadius = 10

    def draw(self):
        pygame.draw.line(self.display, self.color,
                         self.springerModel.head.getTouple(), self.springerModel.foot.getTouple(), self.width)

        pygame.draw.line(self.display, self.weightColor,
                         self.springerModel.getBallPosition().getTouple(), self.springerModel.head.getTouple(), self.width)

        pygame.draw.circle(self.display, self.weightColor, self.springerModel.getBallPosition().getTouple(), self.weightRadius)

