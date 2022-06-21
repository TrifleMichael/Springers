import pygame
import time

from Utility.Settings import RES_X, RES_Y, FRAME_TIME, MAX_GENERATION


def showBestGeneration(levelManager, BLACK_BOX, DISPLAY, prompt = True):

    if prompt:
        print("---------------------------")
        input("PRESS ENTER TO START REPLAY")


    REPLAY = True
    BLACK_BOX.prepareReplay()
    levelManager.updateDisplay(DISPLAY)
    while REPLAY:
        startTime = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                REPLAY = False

        if BLACK_BOX.ifTimeToCreateNewGeneration():
            break

        BLACK_BOX.iterate()
        levelManager.iterate()

        levelManager.draw()
        endTime = time.time()
        if endTime - startTime < FRAME_TIME:
            pygame.time.delay(int((startTime + FRAME_TIME * 1000) - endTime))
        pygame.display.update()

    maxDist = 0
    for springer in levelManager.springerManager.springerList:
        maxDist = max(springer.head.x, maxDist)
    print("Max distance for this generation: ", maxDist)