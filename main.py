import time
import pygame

from Managers.LevelManager import LevelManager
from SpringerModel.Springer import WeighBallState
from Utility.Point import Point
from Utility.Settings import *

DISPLAY = pygame.display.set_mode((RES_X, RES_Y))
RUN = True
levelManager = LevelManager(DISPLAY)

pygame.display.set_caption("Springers Simulation")

levelManager.addControllableSpringer(Point(100, 100), Point(50, 200))

while RUN:

    startTime = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                levelManager.springerManager.updateControlls(WeighBallState.LEFT, None)
            if event.key == pygame.K_s:
                levelManager.springerManager.updateControlls(WeighBallState.MIDDLE, None)
            if event.key == pygame.K_d:
                levelManager.springerManager.updateControlls(WeighBallState.RIGHT, None)

    levelManager.iterate()
    levelManager.draw()

    endTime = time.time()
    if endTime - startTime < FRAME_TIME:
        pygame.time.delay(int((startTime + FRAME_TIME*1000) - endTime))
    pygame.display.update()

