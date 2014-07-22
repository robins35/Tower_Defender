#! /usr/bin/env python

import pygame
from pygame.locals import *
import gameObjs
from managers import snd_man

selec, placeTow, bomb = range(3)
arrowTower, swordTower = range(2)
currentTool = None
currentTower = swordTower

def detectTile(pos = None):
	if pos is None: pos = pygame.mouse.get_pos()
	if pos == (0, 0): return (-1, -1)
	return (pos[0] / 32, pos[1] / 32)

def tileHighlight(validTiles):
	currentTile = detectTile()
	hoverRect = pygame.Rect(currentTile[0]*32, currentTile[1]*32, 32, 32)
	
	if currentTile == (-1, -1) or \
	currentTile[0] > 24 or \
	hoverRect.collidelist([elem.rect.inflate(-22, -30) for elem in gameObjs.tower_sprites]) > -1:
		return 0
	elif currentTile in validTiles:
		gameObjs.hoverTile((currentTile[0]*32, currentTile[1]*32), True)
	else:
		gameObjs.hoverTile((currentTile[0]*32, currentTile[1]*32))

class Bank:
	def __init__(self):
		self.money = 30
		#tower costs:
		self.prices = {
			arrowTower: 30,
			swordTower: 60
		}

		self.hp = 5
		#self.ad = snd_man.get('accessdenied')

class DragSelectController:
	def __init__(self):
		self.drag = False
		self.start = (0, 0)
		self.end = (0, 0)
		self.selectColor = (0, 255, 0)
		self.selected = None
		self.highlightRect = None
		self.rangeSpr = None

	def dragStart(self):
		coords = pygame.mouse.get_pos()
		if detectTile(coords)[0] > 24: return
		self.drag = True
		self.start = coords
		self.rect = pygame.Rect(coords, (1, 1))
		self.lastEnd = self.end

	def dragStep(self, screen, bg):
		self.end = pygame.mouse.get_pos()
		screen.blit(bg, (0, 0))
		self.rect.width = self.end[0] - self.start[0]
		self.rect.height = self.end[1] - self.start[1]
		pygame.draw.rect(screen, self.selectColor, self.rect, 2)
		self.lastEnd = self.end

	def dragEnd(self, screen, bg):
		if self.selected is not None:
			self.selected.rangeSpr.killVisib()
			self.selected = None
		screen.blit(bg, (0, 0))

		try:
			if self.rect is not None: self.rect.normalize()
		except:
			self.drag = False
			self.start, self.end = (0, 0), (0, 0)
			return
		coll_ind = self.rect.collidelist([elem.rect.inflate(-22, -30) for elem in gameObjs.tower_sprites])
		if coll_ind > -1:
			rectlist = [elem.rect for elem in gameObjs.tower_sprites]
			for spr in gameObjs.tower_sprites:
				if spr.rect == rectlist[coll_ind]:
					self.selected = spr
					self.selected.rangeSpr.makeVis()
		self.drag = False
		self.start, self.end = (0, 0), (0, 0)

def placeTower(validTiles):
	currentTile = detectTile()

	if drag_select_controller.selected is not None:
			drag_select_controller.selected.rangeSpr.killVisib()

	if currentTile in validTiles:
		if bank.money < bank.prices[currentTower]:
			snd_man.get('accessdenied').play()
		else:
			bank.money -= bank.prices[currentTower]
			validTiles.remove(currentTile)

			options = {
				arrowTower: lambda pos: gameObjs.Tower((pos[0], pos[1]), 'arrowTower', 'axe', 2),
				swordTower: lambda pos: gameObjs.Tower((pos[0], pos[1]), 'tower1', 'knife', 4)
			}
			drag_select_controller.selected = options[currentTower]((currentTile[0] * 32, currentTile[1] * 32))


def checkTowerEnemColl():
	collDict = pygame.sprite.groupcollide(gameObjs.trange_sprites, gameObjs.enemy_sprites, False, False)

	for r in collDict:
		r.selected.shoot((collDict[r][0].rect.left, collDict[r][0].rect.centery))

	collDict = pygame.sprite.groupcollide(gameObjs.projectile_sprites, gameObjs.enemy_sprites, True, False)

	for r in collDict:
		collDict[r][0].takeDamage(r.damage)

def checkButtonClick():
	click_point = pygame.mouse.get_pos()
	for bt in gameObjs.button_sprites:
		if bt.rect.collidepoint(click_point):
			if bt.action is not None: bt.action()
			return

drag_select_controller = DragSelectController()
bank = Bank()