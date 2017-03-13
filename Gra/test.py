# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:02:29 2017

@author: Rejurhf
"""

import sys
import sdl2
import sdl2.ext
import random
random.seed()

WHITE = sdl2.ext.Color(255,255,255)
RESOURCES = sdl2.ext.Resources(__file__,"res")

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)
        
    def render(self, components):
        sdl2.ext.fill(self.surface, sdl2.ext.Color(1,1,1))
        super(SoftwareRenderer, self).render(components)
        
        
class MovementSyste(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(MovementSyste, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        
    def process(self, world, componentsets):
        for velocity, sprite in componentsets:
            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy
            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)
            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight
            if pmaxx > self.maxx:
                sprite.x = self.maxx - swidth
            if pmaxy > self.maxy:
                sprite.y = self.maxy - sheight
        
                
class CollisionSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(CollisionSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.ball = None
        self.paddle = None
        self.player = None
        self.lis = []
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        
    def _overlap(self, item):
        pos, sprite = item
        if sprite == self.ball.sprite:
            return False
            
        left, top, right, bottom = sprite.area
        bleft, btop, bright, bbottom = self.ball.sprite.area
        
        return (bleft < right and bright > left and
                btop < bottom and bbottom > top)
        
    def process(self, world, componentsets):
        collitems = [comp for comp in componentsets if self._overlap(comp)]
        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        if collitems:
            sprite = collitems[0][1]
            print("P: %d, %d" %(sprite.x, sprite.y))
            if self.paddle.sprite.x == sprite.x:
                self.ball.velocity.vy = -self.ball.velocity.vy
                if(self.ball.sprite.y+20 > self.paddle.sprite.y+7 and
                   self.ball.sprite.x+20 > self.paddle.sprite.x+7 and
                   self.ball.sprite.x < self.paddle.sprite.x+self.paddle.sprite.size[0]-7):
                    self.ball.sprite.y -= 20
                if((self.ball.sprite.x + self.ball.sprite.size[0] >= self.paddle.sprite.x and
                   self.ball.sprite.x + self.ball.sprite.size[0] <= self.paddle.sprite.x+10) or
                   (self.ball.sprite.x <= self.paddle.sprite.x + self.paddle.sprite.size[0] and
                   self.ball.sprite.x >= self.paddle.sprite.x + self.paddle.sprite.size[0]-10)):
                    self.ball.velocity.vx = -self.ball.velocity.vx
                elif self.paddle.velocity.vx > 0 and self.ball.velocity.vx < 5:
                    self.ball.velocity.vx += 1
                    print("V: %d, %d" %(self.ball.velocity.vx, self.ball.velocity.vy))
                elif self.paddle.velocity.vx < 0 and self.ball.velocity.vx > -5:
                    self.ball.velocity.vx -= 1
                    print("V: %d, %d" %(self.ball.velocity.vx, self.ball.velocity.vy))
            else:
                brc = None
                for i in range(0, len(self.lis)):
                    if (self.lis[i].sprite.x == sprite.x and
                        self.lis[i].sprite.y == sprite.y):
                        brc = i
                        break
                if((self.ball.sprite.x + self.ball.sprite.size[0] >= self.lis[brc].sprite.x and
                   self.ball.sprite.x + self.ball.sprite.size[0] <= self.lis[brc].sprite.x+10) or
                   (self.ball.sprite.x <= self.lis[brc].sprite.x + self.lis[brc].sprite.size[0] and
                   self.ball.sprite.x >= self.lis[brc].sprite.x + self.lis[brc].sprite.size[0]-10)):
                    self.ball.velocity.vx = -self.ball.velocity.vx
                else:
                    self.ball.velocity.vy = -self.ball.velocity.vy
                self.lis[brc].sprite = factory.from_color(WHITE, size=(0,0))
                del self.lis[brc]
        if(self.ball.sprite.y <= self.miny):
            self.ball.velocity.vy = -self.ball.velocity.vy
        if(self.ball.sprite.y + self.ball.sprite.size[1] >= self.maxy):
            self.ball.velocity.vx = 0
            self.ball.velocity.vy = 0
            self.ball.sprite.x = self.paddle.sprite.x + 40
            self.ball.sprite.y = self.paddle.sprite.y - 20
            if self.player.zycia == 0:
                self.ball.sprite = factory.from_color(WHITE, size=(0,0))
                self.paddle.sprite = factory.from_color(WHITE, size=(0,0))
                while self.lis:
                    self.lis[0].sprite = factory.from_color(WHITE, size=(0,0))
                    del self.lis[brc]
            self.player.zycia -= 1
        if(self.ball.sprite.x <= self.minx or 
           self.ball.sprite.x + self.ball.sprite.size[0] >= self.maxx):
            self.ball.velocity.vx = -self.ball.velocity.vx
     
            
class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0
        
        
class Paddle(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx, posy):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = Velocity()
        

class Ball(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx, posy):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = Velocity()
        

class Brick(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx, posy):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = Velocity()
        

class Player(object):
    def __init__(self, zycia):
        self.zycia = zycia
    

def run():
    sdl2.ext.init()
    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    window = sdl2.ext.Window("Arkanoid v1", size=(800, 1000))
    window.show()
    world = sdl2.ext.World()
    
    spriteRenderer = SoftwareRenderer(window)
    world.add_system(spriteRenderer)
    movement = MovementSyste(0, 0, 800, 1000)
    world.add_system(movement)
    collision = CollisionSystem(0, 0, 800, 1000)
    world.add_system(collision)

    
    
    sp_paddle = factory.from_color(WHITE, size=(100, 20))
    paddle = Paddle(world, sp_paddle, 350, 980)
    collision.paddle = paddle
    sp_ball = factory.from_color(WHITE, size=(20, 20))
    ball = Ball(world, sp_ball, 390, 960)
    collision.ball = ball
    brickList = []
    for j in range(0, 25):
        poy = 52 + j*22
        for i in range(0, 10):
            pox = 52 + i*42
            sp_brick = factory.from_color(WHITE, size=(40,20))
            brick = Brick(world, sp_brick, pox, poy)
            brickList.append(brick)
    collision.lis = brickList
    player = Player(1)
    collision.player = player
    img = factory.from_image(RESOURCES.get_path("koniecgry.jpg"))
    
    running = True
    flag = False
    while running:
        events = sdl2.ext.get_events()
        if player.zycia < 0:
            world.process()
            break
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    paddle.velocity.vx = 3
                    if(ball.velocity.vx == 0 and ball.velocity.vy == 0 and 
                       ball.sprite.x < 800-62):
                        ball.velocity.vx = 3
                        flag = True
                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    paddle.velocity.vx = -3
                    if(ball.velocity.vx == 0 and ball.velocity.vy == 0 and 
                       ball.sprite.x > 42):
                        ball.velocity.vx = -3
                        flag = True
                if event.key.keysym.sym == sdl2.SDLK_SPACE:
                    if ball.velocity.vx == 0 and ball.velocity.vy == 0:
                        ball.velocity.vy = -3
                        tmp = random.randint(1, 2)
                        if tmp == 1: ball.velocity.vx = -3
                        else: ball.velocity.vx = 3
            elif event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym in (sdl2.SDLK_RIGHT, sdl2.SDLK_LEFT):
                    paddle.velocity.vx = 0
                    if flag:
                        ball.velocity.vx = 0
                        ball.velocity.vy = 0
                        flag = False
                    
        sdl2.SDL_Delay(8)
        world.process()
    
    while running:
        ball = None
        #spriterenderer = factory.create_sprite_render_system(window)
        #spriterenderer.render(img)
        
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            
    return 0

if __name__=="__main__":
    sys.exit(run())