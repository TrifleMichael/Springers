import time
import pygame

from Managers.LevelManager import LevelManager
from SpringerModel.Springer import WeighBallState
from Utility.Point import Point
from Utility.Settings import *

DISPLAY = pygame.display.set_mode((RES_X, RES_Y))
levelManager = LevelManager(DISPLAY)


def mainLoop():
    pygame.display.set_caption("Springers Simulation")
    RUN = True
    levelManager.addControllableSpringer(Point(100, 100), Point(50, 200))

    while RUN:

        startTime = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    levelManager.springerManager.changeBallState(WeighBallState.LEFT)
                if event.key == pygame.K_s:
                    levelManager.springerManager.changeBallState(WeighBallState.MIDDLE)
                if event.key == pygame.K_d:
                    levelManager.springerManager.changeBallState(WeighBallState.RIGHT)
                if event.key == pygame.K_q:
                    levelManager.springerManager.changeSpringState(False)
                if event.key == pygame.K_e:
                    levelManager.springerManager.changeSpringState(True)

        levelManager.iterate()
        levelManager.draw()

        endTime = time.time()
        if endTime - startTime < FRAME_TIME:
            pygame.time.delay(int((startTime + FRAME_TIME*1000) - endTime))
        pygame.display.update()


mainLoop()
