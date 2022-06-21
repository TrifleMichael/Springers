import time
import pygame
import random as rd

from Managers.LevelManager import LevelManager
from SpringerModel.Springer import WeighBallState, SpringState
from Utility.BlackBox import BlackBox
from Utility.Settings import *
from Utility.ShowBestGeneration import showBestGeneration
from Utility.UtilityFunctions import getStartFoot, getStartHead, createRandomGenomeSpringers, getRandomGenome

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
    if not PLAYER_CONTROL:
        createRandomGenomeSpringers(SPRINGERS_PER_GENERATION, levelManager)
    else:
        levelManager.addControllableSpringer(getStartHead(), getStartFoot(), getRandomGenome())

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

        if HEADLESS_MODE and BLACK_BOX.generationNumber == MAX_GENERATION+1:
            RUN = False
            DISPLAY = pygame.display.set_mode((RES_X, RES_Y))
            showBestGeneration(levelManager, BLACK_BOX, DISPLAY)
            ans = input("Show again? (y/n)\n")
            while ans == "y":
                showBestGeneration(levelManager, BLACK_BOX, DISPLAY, prompt=False)
                ans = input("Show again? (y/n)\n")

mainLoop()
