import time
import pygame

from Managers.LevelManager import LevelManager
from SpringerModel.Springer import WeighBallState, SpringState
from Utility.BlackBox import BlackBox
from Utility.Settings import *

DISPLAY = pygame.display.set_mode((RES_X, RES_Y))
levelManager = LevelManager(DISPLAY)
BLACK_BOX = BlackBox(levelManager.springerManager, levelManager)


def mainLoop():
    pygame.display.set_caption("Springers Simulation")
    RUN = True

    levelManager.addControllableSpringer(STARTING_HEAD, START_FOOT, ["D", "N", "A"])
    # Przykladowy springer ktory moze byc kontrolowany przez gracza
    # Chyba ze PLAYER_CONTROL jest wylaczone w ustawieniach, wtedy zarzada nim BLACK_BOX
    # Mozna je tworzyc w petli i moga wspoldzielic pozycje (co najwyzej beda sie zlewaly graficznie)
    # Tablica DNA to symboliczny genom. Zmieniajcie go jak chcecie.
    # TODO: Tworzyc wiele Springerow w petli z roznymi genotypami

    while RUN:

        startTime = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

            if PLAYER_CONTROL:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        levelManager.springerManager.changeBallState(WeighBallState.LEFT)
                    if event.key == pygame.K_s:
                        levelManager.springerManager.changeBallState(WeighBallState.MIDDLE)
                    if event.key == pygame.K_d:
                        levelManager.springerManager.changeBallState(WeighBallState.RIGHT)
                    if event.key == pygame.K_q:
                        levelManager.springerManager.springState = SpringState.RETRACTED
                    if event.key == pygame.K_e:
                        levelManager.springerManager.springState = SpringState.EXTENDED

        if not PLAYER_CONTROL:
            BLACK_BOX.iterate()
        levelManager.iterate()
        levelManager.draw()

        endTime = time.time()
        if endTime - startTime < FRAME_TIME:
            pygame.time.delay(int((startTime + FRAME_TIME*1000) - endTime))
        pygame.display.update()


mainLoop()
