#! /usr/bin/env python

import sys, pygame
from pygame.locals import *
from managers import img_man, snd_man
import maps
import gameObjs
import tools

pygame.init()
size = width, height = 960, 736
#bg = pygame.Surface(size)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

img_man.load_tiles()
img_man.load_sprites()
snd_man.load_Sounds()
maps.loadMaps()

game_controller = gameObjs.GameController(pygame.Surface(size), screen, maps)

spriteCopy = None

while 1:
	clock.tick(60)

	if not game_controller.paused:
		game_controller.update()

		# take care of events
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if tools.checkButtonClick():
					pass
				elif tools.currentTool == tools.selec:
					tools.drag_select_controller.dragStart()
				elif tools.currentTool == tools.placeTow:
					tools.placeTower(maps.towerSpots)
				elif tools.currentTool == tools.bomb:
					gameObjs.sprites.remove(gameObjs.enemy_sprites)
					gameObjs.enemy_sprites.empty()
					game_controller.spawnLeft = 0
			if event.type == pygame.MOUSEBUTTONUP:
				if tools.currentTool == tools.selec:
					tools.drag_select_controller.dragEnd(screen, game_controller.bg)
			if event.type == pygame.KEYDOWN:
				if pygame.key.get_pressed()[K_2] == False:
					if gameObjs.hover_sprite is not None: gameObjs.hover_sprite.kill()
				if pygame.key.get_pressed()[K_1]:
					tools.currentTool = tools.selec
				if pygame.key.get_pressed()[K_2]:
					tools.currentTool = tools.placeTow
				if pygame.key.get_pressed()[K_3]:
					tools.currentTool =  tools.bomb
				if pygame.key.get_pressed()[K_ESCAPE]:
					game_controller.paused = True
				if pygame.key.get_pressed()[K_F1]:
					spriteCopy = gameObjs.sprites.copy()
					gameObjs.sprites.empty()
					game_controller.help = gameObjs.HelpMenu()
					game_controller.paused = True
					continue

		tools.checkTowerEnemColl()

		# run update for each sprite
		for spr in gameObjs.sprites:
			spr.update()

		# Take care of updates inside loop
		if tools.currentTool == tools.selec:
			if tools.drag_select_controller.drag:
				tools.drag_select_controller.dragStep(screen, game_controller.bg)
		elif tools.currentTool == tools.placeTow:
			if(tools.tileHighlight(maps.towerSpots) == 0 and gameObjs.hover_sprite is not None):
				gameObjs.hover_sprite.kill()
	else:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				tools.checkButtonClick()
			if event.type == pygame.KEYDOWN:
				if pygame.key.get_pressed()[K_ESCAPE] and game_controller.gameover == False:
					game_controller.paused = False
				if pygame.key.get_pressed()[K_F1]:
					game_controller.help.kill()
					gameObjs.sprites.add(spriteCopy)
					game_controller.paused = False
	# debugging
	pygame.display.set_caption('Pygame Tutorial 3 - Pong   %d fps - %d - %d - %s' % \
		(clock.get_fps(), len(gameObjs.sprites), len(maps.towerSpots), tools.detectTile()))

	# clear sprites and draw new ones
	gameObjs.sprites.clear(screen, game_controller.bg)
	gameObjs.sprites.draw(screen)
	#pygame.display.update()
	pygame.display.flip()