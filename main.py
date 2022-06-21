import time
import pygame
import random as rd

from Managers.LevelManager import LevelManager
from SpringerModel.Springer import WeighBallState, SpringState
from Utility.BlackBox import BlackBox
from Utility.Settings import *
from Utility.UtilityFunctions import getStartFoot, getStartHead

if not HEADLESS_MODE:
    DISPLAY = pygame.display.set_mode((RES_X, RES_Y))
else:
    DISPLAY = None
levelManager = LevelManager(DISPLAY)
BLACK_BOX = BlackBox(levelManager.springerManager, levelManager)

def interpretKeyboardInput(levelManager):
    if PLAYER_CONTROL:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            levelManager.springerManager.changeBallState(WeighBallState.LEFT)
        if keys[pygame.K_s]:
            levelManager.springerManager.changeBallState(WeighBallState.MIDDLE)
        if keys[pygame.K_d]:
            levelManager.springerManager.changeBallState(WeighBallState.RIGHT)
        if keys[pygame.K_q]:
            levelManager.springerManager.springState = SpringState.RETRACTED
        if keys[pygame.K_e]:
            levelManager.springerManager.springState = SpringState.EXTENDED

def mainLoop():
    if not HEADLESS_MODE:
        pygame.display.set_caption("Springers Simulation")
    RUN = True
    genome1 = [
        (6, 3, 1, 5, 5),
        (1, 3, 6, 9, 1),
        (6, 3, 1, 5, 5),
        (1, 3, 6, 9, 1),
        (6, 3, 1, 5, 5),
        (1, 3, 6, 9, 1),
        (6, 3, 1, 5, 5),
        (1, 3, 6, 9, 1)
        ]
    genome2 = [
        (6, 3, 1, 5, 5),
        (3, 6, 1, 9, 1),
        (6, 3, 1, 5, 5),
        (3, 6, 1, 9, 1),
        (6, 3, 1, 5, 5),
        (3, 6, 1, 9, 1),
        (6, 3, 1, 5, 5),
        (1, 3, 6, 9, 1)
        ]
    genome3 = [
        (6, 3, 1, 5, 5),
        (6, 1, 3, 9, 1),
        (6, 2, 2, 5, 5),
        (7, 2, 1, 9, 1),
        (6, 3, 1, 5, 5),
        (3, 7, 0, 9, 1),
        (6, 3, 1, 5, 5),
        (1, 3, 6, 9, 1)
        ]
    genome4 = [
        (6, 3, 1, 5, 5),
        (6, 1, 3, 9, 1),
        (6, 2, 2, 5, 5),
        (7, 1, 2, 9, 1),
        (6, 2, 2, 5, 5),
        (3, 5, 2, 9, 1),
        (6, 3, 1, 5, 5),
        (1, 3, 6, 9, 1)
        ]
    levelManager.addControllableSpringer(getStartHead(), getStartFoot(), genome1)
    levelManager.addControllableSpringer(getStartHead(), getStartFoot(), genome2)
    levelManager.addControllableSpringer(getStartHead(), getStartFoot(), genome3)
    levelManager.addControllableSpringer(getStartHead(), getStartFoot(), genome4)
    # Przykladowy springer ktory moze byc kontrolowany przez gracza
    # Chyba ze PLAYER_CONTROL jest wylaczone w ustawieniach, wtedy zarzada nim BLACK_BOX
    # Mozna je tworzyc w petli i moga wspoldzielic pozycje (co najwyzej beda sie zlewaly graficznie)
    # Tablica DNA to symboliczny genom. Zmieniajcie go jak chcecie.
    # TODO: Tworzyc wiele Springerow w petli z roznymi genotypami

    while RUN:

        if not HEADLESS_MODE:
            startTime = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False

            interpretKeyboardInput(levelManager)

        if not PLAYER_CONTROL:
            BLACK_BOX.iterate()

        levelManager.iterate()

        if not HEADLESS_MODE:
            levelManager.draw()
            endTime = time.time()
            if endTime - startTime < FRAME_TIME:
                pygame.time.delay(int((startTime + FRAME_TIME*1000) - endTime))
            pygame.display.update()


mainLoop()
