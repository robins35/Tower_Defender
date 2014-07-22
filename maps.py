#! /usr/bin/env python

import pygame
from pygame.locals import *
from managers import img_man

towerSpots = []

def drawMap(screen, mp):
       del towerSpots[:]
       for y in range(len(mp)):
              for x in range(len(mp[y])):
                     location = (x*32, y*32)
                     screen.blit(mp[y][x][0], location)
                     if(mp[y][x] == img_man.get('towerspot')): towerSpots.append((x, y))

def drawHudBG(screen):
       for y in range(23):
              for x in range(25, 30):
                     location = (x*32, y*32)
                     screen.blit(u[0], location)

def loadMaps():
       global MAPS
       global u

       g = img_man.get('grass') #grass
       w = img_man.get('water') #water
       l = img_man.get('land1') #land

       a = img_man.get('landtowater') #landtowater
       b = img_man.get('watertoland') #watertoland
       c = img_man.get('landupwater') #landupwater
       d = img_man.get('waterupland') #waterupland
       e = img_man.get('landwaterbotright') #landwaterbotright
       f = img_man.get('landwaterbotleft') #landwaterbotleft
       h = img_man.get('landwaterupright') #landwaterupright
       i = img_man.get('landwaterupleft') #landwaterupleft
       j = img_man.get('landwaterbotright2') #landwaterbotrigh2
       k = img_man.get('landwaterbotleft2') #landwaterbotleft2
       m = img_man.get('waterlandupleft') #waterlandupleft
       n = img_man.get('waterlandupright') #waterlandupright
       o = img_man.get('landtosand') #landtosand
       p = img_man.get('sandtoland') #sandtoland
       q = img_man.get('sndcrvleftup') #sand curv upper left
       r = img_man.get('sndcrvrightup') #sand curv upper right
       s = img_man.get('sandtowater') #sand to water
       t = img_man.get('watertosand') #water to sand
       u = img_man.get('towerspot') #tower spot
       v = img_man.get('sandupwater') #sand up to water
       x = img_man.get('sandwaterupright')
       y = img_man.get('sandwaterupleft')

       #matrix containing the gattern of tiles to be rendered
       MAPS = {
                     1: [[w,w,w,w,w,w,w,w,w,t,g,g,g,g,g,s,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,t,g,g,g,g,g,s,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,t,g,g,g,g,g,s,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,t,g,g,g,g,g,s,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,i,c,o,v,v,v,q,g,g,g,g,g,r,p,c,c,c,c,h,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,u,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,u,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,u,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,b,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,f,d,d,d,d,d,d,k,g,g,g,j,d,d,d,d,d,d,e,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,b,g,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,b,g,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,b,g,g,g,a,w,w,w,w,w,w,w,w,w,w],
                     [w,w,w,w,w,w,w,w,w,w,b,g,g,g,a,w,w,w,w,w,w,w,w,w,w]],

                     2: [[w,w,w,w,w,w,w,w,w,w,w,t,g,s,w,w,w,w,w,t,g,a,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,t,g,s,w,w,w,w,w,t,g,a,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,t,g,s,w,w,w,w,w,t,g,a,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,t,g,s,w,w,w,w,w,t,g,a,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,t,g,s,w,i,c,h,w,t,g,a,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,t,g,s,w,b,u,a,w,t,g,a,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,t,g,s,w,f,d,e,w,t,g,a,w,w,w],\
                     [w,w,w,w,w,w,w,y,v,v,v,q,g,r,v,v,v,v,v,q,g,a,w,w,w],\
                     [w,w,w,w,w,w,w,t,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [w,w,w,w,w,w,w,t,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [v,v,v,v,v,x,w,t,g,g,g,u,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [g,g,g,g,g,r,v,q,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,a,w,w,w],\
                     [d,d,d,d,d,d,d,d,d,d,d,k,g,g,j,d,d,d,d,d,d,e,w,w,w],\
                     [w,w,w,w,w,w,w,i,c,h,w,b,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,b,u,a,w,b,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,f,d,e,w,b,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,b,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,b,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,b,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,b,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,b,g,g,a,w,w,w,w,w,w,w,w,w,w],\
                     [w,w,w,w,w,w,w,w,w,w,w,b,g,g,a,w,w,w,w,w,w,w,w,w,w]],

                     'splash':     [[u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u],
                                   [u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u,u] ],

                     'gameover': [[g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,w,w,w,g,g,g,g,w,g,g,g,w,g,g,g,w,g,w,w,w,w,g,g,g,g,g],
                                   [g,g,g,w,g,g,g,g,g,g,w,g,w,g,g,w,w,g,w,w,g,w,g,g,g,g,g,g,g,g],
                                   [g,g,g,w,g,g,w,w,g,g,w,w,w,g,g,w,g,w,g,w,g,w,w,w,g,g,g,g,g,g],
                                   [g,g,g,w,g,g,g,w,g,w,g,g,g,w,g,w,g,w,g,w,g,w,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,w,w,w,w,g,w,g,g,g,w,g,w,g,g,g,w,g,w,w,w,w,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,w,w,g,g,w,g,g,g,w,g,g,w,w,w,w,g,g,w,w,w,g,g,g,g,g,g],
                                   [g,g,g,w,g,g,w,g,w,g,g,g,w,g,g,w,g,g,g,g,g,w,g,g,w,g,g,g,g,g],
                                   [g,g,g,w,g,g,w,g,g,w,g,w,g,g,g,w,w,w,g,g,g,w,w,w,w,g,g,g,g,g],
                                   [g,g,g,w,g,g,w,g,g,w,g,w,g,g,g,w,g,g,g,g,g,w,w,g,g,g,g,g,g,g],
                                   [g,g,g,g,w,w,g,g,g,g,w,g,g,g,g,w,w,w,w,g,g,w,g,w,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g],
                                   [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g] ]
              }