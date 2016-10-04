import pyscreenshot as imagegrab
import os
import time
from PIL import ImageOps
import numpy as np


def screengrab():
    box = (660,180,1260,1056)
    im = imagegrab.grab(box)
    im.save(os.getcwd() + str(int(time.time())) + '.png', 'PNG')


def get_arbol_izq():
    box = (660+206,180+353,660+206+68,180+353+37)
    im = ImageOps.grayscale(imagegrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    # im.save(os.getcwd() + 'get_arbol_izq_' + str(int(time.time())) + '.png', 'PNG')
    return np.asscalar(a)


def get_arbol_der():
    box = (660+325,180+353,660+325+68,180+353+37)
    im = ImageOps.grayscale(imagegrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    # im.save(os.getcwd() + 'get_arbol_izq_' + str(int(time.time())) + '.png', 'PNG')
    return np.asscalar(a)

screengrab()