import pygame.draw

from Utility.Settings import RES_Y, RES_X, FLOOR_HEIGHT


class DrawManager:
    def __init__(self, display):
        self.display = display

        self.floorColor = (0, 100, 0)
        self.backGroundColor = (0, 0, 20)

        self.springerSpriteList = []

    def addSpringerSprite(self, sprigerSprite):
        self.springerSpriteList.append(sprigerSprite)

    def draw(self):
        self.display.fill(self.backGroundColor)
        pygame.draw.rect(self.display, self.floorColor, (0, RES_Y - FLOOR_HEIGHT, RES_X, FLOOR_HEIGHT))

        for springerSprite in self.springerSpriteList:
            springerSprite.draw()