import time
import pygame
import random as rd

from Managers.LevelManager import LevelManager
from SpringerModel.Springer import WeighBallState, SpringState
from Utility.BlackBox import BlackBox
from Utility.Settings import *
from Utility.ShowBestGeneration import showBestGeneration
from Utility.UtilityFunctions import getStartFoot, getStartHead, createRandomGenomeSpringers

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
    createRandomGenomeSpringers(SPRINGERS_PER_GENERATION, levelManager)
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

        if HEADLESS_MODE and BLACK_BOX.generationNumber == MAX_GENERATION:
            RUN = False
            showBestGeneration(levelManager, BLACK_BOX)

mainLoop()
