#! /usr/bin/env python

import os, pygame
from pygame.locals import *

class ImageManager:
    def __init__(self):
        self.dict = {}

        """ width = 16
        surf = pygame.Surface((width,width))
        r = surf.get_rect()
        surf.fill((255,255,255))
        surf.set_colorkey((255,255,255))
        pygame.draw.line(surf,(0,0,0),(0,width/2),(width,width/2),1)
        pygame.draw.line(surf,(0,0,0),(width/2,0),(width/2,width),1)
        self.dict["cursor"] = surf, surf.get_rect()"""
        
    def get(self, name):
        return self.dict[name]
    
    def load_image(self, name, colorkey=None):
        """Loads a single image file and returns it"""
        dictname = name[0:name.find('.')]
        fullname = os.path.join('images', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print (('Cannot load image:', fullname))
            raise SystemExit( message)
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        self.dict[dictname] = image, image.get_rect()

    def load_strip(self, name, width, height, colorkey=None):
        """Loads images from a strip file and stores it in dict under name.
        Images can be packed in rows and columns."""
        dictname = name[0:name.find('.')]
        self.load_image(name, colorkey)
        image, rect = self.dict[dictname]
        images = []
        for y in range(0, image.get_height(), height):
            for x in range(0, image.get_width(), width):
                newimage = pygame.Surface((width,height))
                newimage.blit(image,(0,0),pygame.Rect(x, y, width, height))
                newimage.convert()
                if colorkey is not None:
                    if colorkey is -1:
                        colorkey = newimage.get_at((0,0))
                    newimage.set_colorkey(colorkey, RLEACCEL)
                images.append(newimage)
        self.dict[dictname] = images, images[0].get_rect()

    def load_tiles(self):
        self.load_image('grass.bmp') #grass
        self.load_image('water.bmp') #water
        self.load_image('land1.png') #land

        self.load_image('landtowater.bmp') #landtowater
        self.load_image('watertoland.bmp') #watertoland
        self.load_image('landupwater.bmp') #landupwater
        self.load_image('waterupland.bmp') #waterupland
        self.load_image('landwaterbotright.bmp') #landwaterbotright
        self.load_image('landwaterbotleft.bmp') #landwaterbotleft
        self.load_image('landwaterupright.bmp') #landwaterupright
        self.load_image('landwaterupleft.bmp') #landwaterupleft
        self.load_image('landwaterbotright2.bmp') #landwaterbotrigh2
        self.load_image('landwaterbotleft2.bmp') #landwaterbotleft2
        self.load_image('waterlandupleft.bmp') #waterlandupleft
        self.load_image('waterlandupright.bmp') #waterlandupright
        self.load_image('landtosand.bmp') #landtosand
        self.load_image('sandtoland.bmp') #sandtoland
        self.load_image('sndcrvleftup.bmp') #sand curv upper left
        self.load_image('sndcrvrightup.bmp') #sand curv upper right
        self.load_image('sandtowater.bmp') #sand to water
        self.load_image('watertosand.bmp') #water to sand
        self.load_image('towerspot.png') # tower spot
        self.load_image('sandupwater.bmp') # sand up to water
        self.load_image('sandwaterupright.bmp')
        self.load_image('sandwaterupleft.bmp')
        self.load_image('helpmenu.png')

    def load_sprites(self):
        self.load_image('baseobj.png', -1) #base object
        #self.load_image('knife.bmp', -1) #test knife
        self.load_image('tower1.png', -1) #first tower
        self.load_image('arrowTower.png', -1) #arrow tower
        self.load_image('redtile.png') #red hover tile
        self.load_image('greentile.png') #green hover tile
        
        self.load_image('axe.bmp', -1)

        # Loading all the knives
        self.load_image('knifeN.bmp', -1)
        self.load_image('knifeS.bmp', -1)
        self.load_image('knifeE.bmp', -1)
        self.load_image('knifeW.bmp', -1)
        self.load_image('knifeNW.bmp', -1)
        self.load_image('knifeNE.bmp', -1)
        self.load_image('knifeSE.bmp', -1)
        self.load_image('knifeSW.bmp', -1)

        ## ANIMATED ANIMATED ANIMATED

        self.load_strip('boomerang.png', 64, 64, -1)

        # Loading Pirate
        self.load_strip('pirateN.png', 29, 44, -1)
        self.load_strip('pirateS.png', 28, 44, -1)
        self.load_strip('pirateE.png', 36, 41, -1)
        self.load_strip('pirateW.png', 36, 41, -1)

        # Loading Ogre
        self.load_strip('ogreN.png', 41, 58, -1)
        self.load_strip('ogreS.png', 45, 50, -1)
        self.load_strip('ogreE.png', 50, 56, -1)
        self.load_strip('ogreW.png', 41, 56, -1)

class SoundManager:
    def __init__(self):
        self.dict = {}
            
    def get(self,name):
        return self.dict[name]
    
    def load_sound(self, name):
        """Loads a sound from a file."""
        class NoneSound:
            def play(self): pass
        if not pygame.mixer or not pygame.mixer.get_init():
            sound = NoneSound()
        else:
            fullname = os.path.join('sounds', name)
            try:
                sound = pygame.mixer.Sound(fullname)
            except pygame.error as message:
                print (('Cannot load sound:', fullname))
                raise SystemExit( message)
        dictname = name[0:name.find('.')]
        self.dict[dictname] = sound

    def load_Sounds(self):
        self.load_sound('arrow_shoot2.wav')
        self.load_sound('intro.wav')
        self.load_sound('accessdenied.wav')
        self.load_sound('coincollect.wav')
        self.load_sound('gameover.wav')
        self.load_sound('gamecomplete.wav')

img_man = ImageManager()
snd_man = SoundManager()