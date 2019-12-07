'''
This code contains BulletSupply and BombSupply classes

By generate BulletSupply/BombSupply instance in main.py, it can be used to 
generate supplys for the hero plane in the game.

**Functions**
	__init__:
		init the self parameters of BulletSupply/BombSupply instance
	move:
		control the BulletSupply/BombSupply to keep moving up on the game interface.
	reset:
		reset the BulletSupply/BombSupply
'''

import pygame
from random import *

class BulletSupply(pygame.sprite.Sprite):
	def __init__(self,bg_size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/ufo1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.width = bg_size[0]
		self.height = bg_size[1]
		self.rect.left = randint(0,self.width - self.rect.width)
		self.rect.bottom = -90
		self.speed = 6
		self.active = False
		self.mask = pygame.mask.from_surface(self.image)

	def move(self):
		if self.rect.top < self.height:
			self.rect.top += self.speed
		else:
			self.active = False

	def reset(self):
		self.active = True
		self.rect.left = randint(0,self.width - self.rect.width)
		self.rect.bottom = -90

class BombSupply(pygame.sprite.Sprite):
	def __init__(self,bg_size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/ufo2.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.width = bg_size[0]
		self.height = bg_size[1]
		self.rect.left = randint(0,self.width - self.rect.width)
		self.rect.bottom = -90
		self.speed = 6
		self.active = False
		self.mask = pygame.mask.from_surface(self.image)

	def move(self):
		if self.rect.top < self.height:
			self.rect.top += self.speed
		else:
			self.active = False

	def reset(self):
		self.active = True
		self.rect.left = randint(0,self.width - self.rect.width)
		self.rect.bottom = -90