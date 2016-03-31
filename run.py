#!/usr/bin/python3
    #Hello, ye curious user! We've outlined what we're doing so you can follow along. If you want to change anything, you're welcome to do so. Just back up this file before you do. Oh, and things we commented out for the sake of developing (and not to guide you) have a space right after the hash sign.
#Imports
import pygame
import sys
import os
import time
from pygame.locals import *
import levels.levelzero
import levels.levelone
#First level
#The actual code of the following levelWhatever() pieces are in their respetive names, in the /bin folder. Check them out!
levels.levelzero.levelZero()
levels.levelone.levelOne()
