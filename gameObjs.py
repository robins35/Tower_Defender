#! /usr/bin/env python

import sys, pygame
from pygame.locals import *
import tools
from managers import img_man, snd_man

sprites = pygame.sprite.RenderPlain()
tower_sprites = pygame.sprite.RenderPlain()
trange_sprites = pygame.sprite.RenderPlain()
enemy_sprites = pygame.sprite.RenderPlain()
projectile_sprites = pygame.sprite.RenderPlain()
button_sprites = pygame.sprite.RenderPlain()
hover_sprite = None

class GameController:
	def __init__(self, bg, screen, maps):
		self.playmode = 'splash'
		self.paused = False
		self.bg = bg
		self.screen = screen
		self.maps = maps
		self.monHud = None
		self.healthHud = None
		self.gameover = False
		self.help = None

		self.levels = 2
		self.currentLevel = 1

		self.lastWave = 0
		self.currentWave = 0
		self.spawnLeft = 0

		self.spawnAlarm = -1
		self.playAlarm = -1


		# The first element is the total number of indices
		self.paths = ((5, (0, 200), (100, 0), (0, 200), (-100, 0), (0, 400)),\
					(5, (0, 200), (-200, 0), (0, 200), (195, 0), (0, 400) ),\
					(4, (0, 220), (150, 0), (0, 120), (-600, 0) ),\
					(5, (0, 380), (-140, 0), (0, -140), (410, 0), (0, -500)),\
					(9, (0, 180), (205, 0), (0, 100), (-350, 0), (0, 100), (370, 0), (0, 180), (-180, 0), (0, 300)),\
					(7, (0, 220), (150, 0), (0, 140), (-250, 0), (0, -130), (130, 0), (0, -300)) )

		self.enemyTypes = {
			'pirate': lambda wv: enemy(wv[2], self.paths[wv[3]], 1, 'pirateS', 10),
			'ogre': lambda wv: enemy(wv[2], self.paths[wv[3]], 2, 'ogreS', 4)
		}

		# EnemyType, SpawnNumber, Starting Position, Path, Delay
		# 1: Pirates - 
		self.waves = {
			1: (('pirate', 3, (360, 5), 0, 50), ('ogre', 4, (360, 5), 1, 100),\
				('pirate', 5, (365, 5), 4, 50)),
			2: (('ogre', 3, (370, 5), 2, 50), ('pirate', 6, (385, 5), 3, 100),\
				('ogre', 5, (370, 5), 5, 120))
		}

	def loadMenu(self, name):
		self.maps.drawMap(self.bg, self.maps.MAPS[name])
		self.screen.blit(self.bg, (0, 0))

	def loadLvl(self):
		self.bg.fill((50, 50, 50))
		self.maps.drawMap(self.bg, self.maps.MAPS[self.currentLevel])
		self.maps.drawHudBG(self.bg)
		self.screen.blit(self.bg, (0, 0))
		self.lastWave = len(self.waves[self.currentLevel])
		self.currentWave = 0
		self.drawHud()
		self.spawnAlarm = 100

	def startPlaying(self):
		self.playmode = 'norm'
		sprites.remove(button_sprites)
		button_sprites.empty()
		self.loadLvl()

	def selectTower(self, twr_name):
		tools.currentTool = tools.placeTow
		if twr_name == 'arrow': tools.currentTower = tools.arrowTower
		elif twr_name == 'sword': tools.currentTower = tools.swordTower

	def enableSelectTool(self):
		tools.currentTool = tools.selec

	def drawHud(self): 
		self.monHud = Button((820, 200), (120, 40), "$: %d" % tools.bank.money, "Square.ttf", 25, (120, 120, 120, 0), lambda: self.selectTower('arrow'))
		self.healthHud = Button((820, 250), (120, 40), "HEALTH: %d" % tools.bank.hp, "Square.ttf", 25, (120, 120, 120, 0), lambda: self.selectTower('arrow'))
		Button((810, 320), (140, 40), "SELECT TOOL", "Square.ttf", 20, (200, 200, 200, 156), self.enableSelectTool)
		Button((820, 500), (120, 40), "Arrow-30", "Square.ttf", 20, (200, 200, 200, 156), lambda: self.selectTower('arrow'))
		Button((820, 570), (120, 40), "Sword-60", "Square.ttf", 20, (200, 200, 200, 156), lambda: self.selectTower('sword'))

	def update(self):
		if self.spawnAlarm > 0: self.spawnAlarm -= 1
		if self.playAlarm > 0: self.playAlarm -= 1

		if self.monHud is not None: self.monHud.text = "$: %d" % tools.bank.money
		if self.healthHud is not None: self.healthHud.text = "HEALTH: %d" % tools.bank.hp

		if tools.bank.hp <= 0:
			snd_man.get('intro').stop()
			snd_man.get('gameover').play()
			tools.currentTool = None
			sprites.empty()
			self.paused = True
			self.gameover = True
			self.loadMenu('gameover')

		if self.playmode == 'norm':
			wv = self.waves[self.currentLevel][self.currentWave-1]
			#print wv

			if self.spawnLeft == 0:
				self.spawnAlarm = -1
				if self.currentWave == self.lastWave:
					if len(enemy_sprites) == 0:
						if self.currentLevel == self.levels:
								snd_man.get('intro').stop()
								snd_man.get('gamecomplete').play()
								tools.currentTool = None
								sprites.empty()
								self.paused = True
								self.gameover = True
								self.loadMenu('gameover')
						else:
							sprites.empty()
							tools.currentTool = tools.selec
							self.currentLevel += 1
							self.loadLvl()

				else:
					if len(enemy_sprites) == 0:
						self.currentWave += 1
						wv = self.waves[self.currentLevel][self.currentWave-1]
						self.spawnLeft = wv[1]
						self.spawnAlarm = 300

			if self.spawnAlarm == 0:
				self.enemyTypes[wv[0]](wv)
				self.spawnLeft -= 1
				self.spawnAlarm = wv[4]
		elif self.playmode == 'splash':
			snd_man.get('intro').play()
			self.loadMenu('splash')
			Button((250, 50), (450, 200), "TOWER", "Team401.ttf", 65, (120, 120, 120, 0))
			Button((160, 200), (650, 200), "DEFENDER", "Team401.ttf", 65, (120, 120, 120, 0))
			Button((350, 370), (250, 80), " PLAY!", "Farcry.ttf", 65, (120, 120, 120, 156), self.startPlaying)
			Button((400, 470), (150, 60), "ABOUT", "Farcry.ttf", 40, (120, 120, 120, 156))
			Button((420, 550), (110, 60), "EXIT", "Farcry.ttf", 40, (120, 120, 120, 156), sys.exit)
			self.playmode = None

class BaseVisual(pygame.sprite.Sprite):
	def __init__(self, xy):
		pygame.sprite.Sprite.__init__(self)
		self.rect.left, self.rect.top = xy
		sprites.add(self)


class HelpMenu(BaseVisual):
	def __init__(self):
		self.image, self.rect = img_man.get('helpmenu')
		BaseVisual.__init__(self, (0, 0))

class Button(BaseVisual):
	def __init__(self, xy, wh, text, font, size, color, func = None):
		self.action = func
		self.image = pygame.Surface(wh, pygame.SRCALPHA, 32)
		self.image = self.image.convert_alpha()
		self.image.fill(color)
		self.text = text
		self.color = color
		pygame.display.set_caption(text)		
		self.my_font = pygame.font.Font(font, size)
		label = self.my_font.render(self.text, 1, (0, 0, 0))
		self.image.blit(label, (10, 5))
		self.rect = self.image.get_rect()
		BaseVisual.__init__(self, xy)
		button_sprites.add(self)
	def update(self):
		self.image.fill(self.color)
		label = self.my_font.render(self.text, 1, (0, 0, 0))
		self.image.blit(label, (10, 5))

class hoverTile(BaseVisual):
	def __init__(self, xy, green = False):
		global hover_sprite
		if green:
			self.image, self.rect = img_man.get('greentile')
		else:
			self.image, self.rect = img_man.get('redtile')

		BaseVisual.__init__(self, xy)
		self.rect.left, self.rect.top = xy
		if hover_sprite is not None: hover_sprite.kill()
		hover_sprite = self

class rangeCirc(BaseVisual):
	def __init__(self, xy, r, selec):
		self.selected = selec
		self.image = pygame.Surface((2*r, 2*r), pygame.SRCALPHA, 32)
		self.image = self.image.convert_alpha()
		self.color = (0, 0, 255, 64)
		self.radius = r
		pygame.draw.circle(self.image, self.color, (r, r), r, 0)
		self.image_bak = self.image
		self.image_invis = pygame.Surface((0, 0))

		coords = (r - 32, r + 8)
		pygame.draw.rect(self.image, (0, 255, 0), pygame.Rect(coords, (56, 38)), 5)

		self.rect = self.image.get_rect()
		BaseVisual.__init__(self, xy)
		trange_sprites.add(self)

	def makeVis(self):
		self.image = self.image_bak

	def killVisib(self):
		self.image = self.image_invis

	def update(self):
		self.rect.center = self.selected.rect.center

class Tower(BaseVisual):
	def __init__(self, xy, img_name, projectile_name, damage):
		self.offstx = -2
		self.offsty = -48
		img = img_man.get(img_name)
		self.image = img[0]
		self.rect = img[1].copy()
		BaseVisual.__init__(self, xy)
		self.rect.move_ip(self.offstx, self.offsty)
		tower_sprites.add(self)
		self.range = 5
		self.rangeSpr = rangeCirc((self.rect.left, self.rect.top), self.range*32, self)
		self.damage = damage
		self.delay = 0
		self.proj_name = projectile_name
		self.shooting_sound = snd_man.get('arrow_shoot2')

	def shoot(self, target):
		if self.delay <= 0:
			self.shooting_sound.play()
			projectile(target, self, self.proj_name, self.damage)
			self.delay = 30

	def update(self):
		if self.delay > 0: self.delay -= 1

class projectile(BaseVisual):
	def __init__(self, target, shooter, imgName, damage):
		self.speed = 10
		self.target = target
		self.shooter = shooter
		self.damage = damage

		if (self.velocity[0] / self.speed) < -.35:
			h = 'W'
		elif (self.velocity[0] / self.speed) > .35:
			h = 'E'
		else: h = ''

		if (self.velocity[1] / self.speed) < -.35: v = 'N'
		elif (self.velocity[1] / self.speed) > .35: v = 'S'
		else: v = ''

		if imgName == 'knife': img = img_man.get('knife' + v + h)
		else: img = img_man.get(imgName)
		#img = img_man.get('knife')

		self.image, self.rect = img[0], img[1].copy()
		BaseVisual.__init__(self, (shooter.rect.left, shooter.rect.top))
		projectile_sprites.add(self)


	@property
	def velocity(self):
		hratio = self.target[0] - self.shooter.rect.left
		vratio = self.target[1] - self.shooter.rect.top
		#print hratio, vratio

		if abs(vratio) > abs(hratio):
			hratio = hratio  * (1.0 / abs(vratio))
			if vratio < 0: vratio = -1
			else: vratio = 1
		else:
			vratio = vratio  * (1.0 / abs(hratio))
			if hratio < 1: hratio = -1
			else: hratio = 1

		#print hratio, vratio
		return (self.speed * hratio, self.speed * vratio)
	 
	def update(self):
		self.rect.move_ip(self.velocity)
		if self.rect.left < 0 or self.rect.left > 960 or self.rect.top < 0 or self.rect.top > 736:
			self.kill()

class enemy(BaseVisual):
	def __init__(self, xy, path, speed, img_name, hp):
		self.hp = hp
		self.path = path
		self.currentVert = 1
		self.lastVert = path[0]
		self.speed = speed
		self.reward = 10

		self.img_name = img_name
		img = img_man.get(img_name)
		self.facing = 'S'
		self.images, self.rect = img[0], img[1].copy()
		self.frame = 0
		self.aspeed = 0.2
		self.nframes = len(self.images)
		self.image = self.images[self.frame]
		BaseVisual.__init__(self, xy)
		self.target = (self.rect.left + self.path[self.currentVert][0], \
		self.rect.top + self.path[self.currentVert][1])
		self.pathRect = pygame.Rect(self.rect.left, self.rect.top, 10, 10)
		enemy_sprites.add(self)


	@property
	def velocity(self):
		hratio = self.path[self.currentVert][0]
		vratio = self.path[self.currentVert][1]
		#print hratio, vratio

		if abs(vratio) > abs(hratio):
			hratio = hratio  * (1.0 / abs(vratio))
			if vratio < 0: vratio = -1
			else: vratio = 1
		else:
			vratio = vratio  * (1.0 / abs(hratio))
			if hratio < 1: hratio = -1
			else: hratio = 1

		#print hratio, vratio
		return (self.speed * hratio, self.speed * vratio)

	def takeDamage(self, amount):
		self.hp -= amount
		if self.hp <= 0:
			snd_man.get('coincollect').play()
			tools.bank.money += self.reward
			self.kill()

	def update(self):
		if self.pathRect.collidepoint(self.target):
			if self.currentVert == self.lastVert:
				self.target = (self.rect.left, self.rect.top)
			else:
				self.currentVert += 1
				self.target = (self.rect.left + self.path[self.currentVert][0], \
				self.rect.top + self.path[self.currentVert][1])
		else:
			self.rect.move_ip(self.velocity)
			self.pathRect.move_ip(self.velocity)

		self.frame = (self.aspeed+self.frame)
		while self.frame >= self.nframes:
			self.frame -= self.nframes
		self.image = self.images[int(self.frame)]

		if self.velocity[0] < 0 and self.facing != 'W':
			img = img_man.get(self.img_name[:-1] + 'W')
			self.facing = 'W'
			self.images = img[0]
			self.frame = 0
			self.nframes = len(self.images)
			self.image = self.images[self.frame]
		elif self.velocity[0] > 0 and self.facing != 'E':
			img = img_man.get(self.img_name[:-1] + 'E')
			self.facing = 'E'
			self.images = img[0]
			self.frame = 0
			self.nframes = len(self.images)
			self.image = self.images[self.frame]
		elif self.velocity[1] > 0 and self.facing != 'S':
			img = img_man.get(self.img_name[:-1] + 'S')
			self.facing = 'S'
			self.images = img[0]
			self.frame = 0
			self.nframes = len(self.images)
			self.image = self.images[self.frame]
		elif self.velocity[1] < 0 and self.facing != 'N':
			img = img_man.get(self.img_name[:-1] + 'N')
			self.facing = 'N'
			self.images = img[0]
			self.frame = 0
			self.nframes = len(self.images)
			self.image = self.images[self.frame]

		if self.rect.left < 0 or self.rect.left > 960 or self.rect.top < 0 or self.rect.top > 736:
			self.escape()

	def escape(self):
		tools.bank.hp -= 1
		self.kill()