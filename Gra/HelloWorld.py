# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 17:30:13 2016
HelloWorld.py
@author: Rejurhf
"""

import sys
import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__,"res")

def run():
    sdl2.ext.init()

    window = sdl2.ext.Window("Hello World", size=(700, 352))
    window.show()

    if "-hardware" in sys.argv:
        print("Using hardware acceleration")
        renderer = sdl2.ext.Renderer(window)
        factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    else:
        print("Using software rendering")
        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

    sprite = factory.from_image(RESOURCES.get_path("test.jpg"))
    
    spriterenderer = factory.create_sprite_render_system(window)
    spriterenderer.render(sprite)

    processor = sdl2.ext.TestEventProcessor()
    processor.run(window)

    sdl2.ext.quit()
    return 0
    
if __name__=="__main__":
    sys.exit(run())