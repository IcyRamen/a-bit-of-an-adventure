import pygame
import sys
import os
import time
from pygame.locals import *

white = (255, 255, 255)
darkGray = (25, 25, 25)
lightGray = (200, 200, 200)
black = (0, 0, 0)
grayBlue = (24, 79, 94)
darkBlue = (54, 53, 151)
darkGreen = (0, 133, 3)
darkPurple = (74, 0, 121)
darkRed = (136, 9, 0)
mainLoop = True
fps = 30
fpsTime = pygame.time.Clock()


def levelZero():
    # Initializing
    pygame.init()
    setDisplay = pygame.display.set_mode((960, 540), FULLSCREEN)
    rightBorder = 960
    bottomBorder = 540
    icon = pygame.image.load(os.path.join('.', 'bin', 'Icon.png')).convert_alpha()
    pygame.display.set_caption('A Bit of an Adventure')
    pygame.display.set_icon(icon)
    # Initial functions
    pygame.mixer.music.load(os.path.join('.', 'bin', 'Intro_8-Bit.wav'))
    pygame.mixer.music.play(-1, 0.0)
    font = pygame.font.Font(os.path.join('.', 'bin', 'NOVEMBER.TTF'), 26)
    playText = font.render("Play", True, lightGray)
    settingsText = font.render("Options", True, lightGray)
    setDisplay.fill(darkGray)
    levelZeroCompleted = False
    # Main loop
    while mainLoop:
        # Check for level completion
        if levelZeroCompleted == True:
            return
        # Drawing, etc.
        playText_rect = playText.get_rect(topleft=(rightBorder / 2 - playText.get_width() / 2 - 200, bottomBorder / 2 - playText.get_height() / 2 + 120))
        settingsText_rect = settingsText.get_rect(topleft=(rightBorder / 2 - playText.get_width() / 2 + 200, bottomBorder / 2 - settingsText.get_height() / 2 + 120))
        setDisplay.fill(darkGray)
        setDisplay.blit(settingsText, settingsText_rect)
        setDisplay.blit(playText, playText_rect)
        setDisplay.blit(icon, (rightBorder / 2 - icon.get_width() / 2, bottomBorder / 2 - icon.get_height() / 2 - 80))
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                print('Goodbye!')
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if playText_rect.collidepoint(pygame.mouse.get_pos()):
                    levelZeroCompleted = True
            # Checking keys
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print('Escape pressed. See ya later!')
                    pygame.quit()
                    sys.exit()
                elif event.key == K_LEFT:
                    playText = font.render("Play", True, grayBlue)
                    playText_rect = playText.get_rect(topleft=(rightBorder / 2 - playText.get_width() / 2 - 200, bottomBorder / 2 - playText.get_height() / 2 + 120))
                    setDisplay.blit(playText, playText_rect)
                elif event.key == K_RIGHT:
                    settingsText = font.render("Options", True, grayBlue)
                    settingsText_rect = settingsText.get_rect(topleft=(rightBorder / 2 - playText.get_width() / 2 + 200, bottomBorder / 2 - settingsText.get_height() / 2 + 120))
                    setDisplay.blit(settingsText, settingsText_rect)
        # Highlighting text on hover
        if settingsText_rect.collidepoint(pygame.mouse.get_pos()):
            settingsText = font.render("Options", True, grayBlue)
            settingsText_rect = settingsText.get_rect(topleft=(rightBorder / 2 - playText.get_width() / 2 + 200, bottomBorder / 2 - settingsText.get_height() / 2 + 120))
            setDisplay.blit(settingsText, settingsText_rect)
        elif playText_rect.collidepoint(pygame.mouse.get_pos()):
            playText = font.render("Play", True, grayBlue)
            playText_rect = playText.get_rect(topleft=(rightBorder / 2 - playText.get_width() / 2 - 200, bottomBorder / 2 - playText.get_height() / 2 + 120))
            setDisplay.blit(playText, playText_rect)
        else:
            playText = font.render("Play", True, lightGray)
            settingsText = font.render("Options", True, lightGray)
        pygame.display.update()
        fpsTime.tick(fps)
