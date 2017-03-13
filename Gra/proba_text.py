# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 09:26:02 2017
proba_text.py
@author: Rejurhf
"""

import sys
import ctypes
from sdl2 import *

def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Hello World",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              592, 460, SDL_WINDOW_SHOWN)
    windowsurface = SDL_GetWindowSurface(window)

    image = SDL_LoadBMP(b"image.bmp")
    SDL_BlitSurface(image, None, windowsurface, None)

    SDL_UpdateWindowSurface(window)
    SDL_FreeSurface(image)

    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break

    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())