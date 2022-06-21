import pygame
import time

from Utility.Settings import RES_X, RES_Y, FRAME_TIME, MAX_GENERATION


def showBestGeneration(levelManager, BLACK_BOX):
    DISPLAY = pygame.display.set_mode((RES_X, RES_Y))
    REPLAY = True
    BLACK_BOX.prepareReplay()
    levelManager.updateDisplay(DISPLAY)
    while REPLAY:
        startTime = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        BLACK_BOX.iterate()
        levelManager.iterate()

        if BLACK_BOX.generationNumber == MAX_GENERATION + 1:
            break

        levelManager.draw()
        endTime = time.time()
        if endTime - startTime < FRAME_TIME:
            pygame.time.delay(int((startTime + FRAME_TIME * 1000) - endTime))
        pygame.display.update()