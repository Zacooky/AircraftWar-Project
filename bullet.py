'''
This code contains bullet1/bullet2 classes

By generate bullet instance in main.py, it can be used to 
generate bullets in the game.

**Functions**
	__init__:
		init the self parameters of bullet1/bullet2 instance
	move:
		control the bullet1/bullet2 to keep moving up on the game interface.
	reset:
		reset the bullet1/bullet2
'''

import pygame

class Bullet1(pygame.sprite.Sprite):
	def __init__(self,position):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/bullet1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left = position[0]
		self.rect.top = position[1]
		self.speed = 12
		self.active = False
		self.mask = pygame.mask.from_surface(self.image)

	def move(self):
		self.rect.top -= self.speed

		if self.rect.top <= 0:
			self.active = False

	def reset(self, position):
		self.rect.left = position[0]
		self.rect.top = position[1]
		self.active = True

class Bullet2(pygame.sprite.Sprite):
	def __init__(self,position):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/bullet2.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left = position[0]
		self.rect.top = position[1]
		self.speed = 15
		self.active = False
		self.mask = pygame.mask.from_surface(self.image)

	def move(self):
		self.rect.top -= self.speed

		if self.rect.top <= 0:
			self.active = False

	def reset(self, position):
		self.rect.left = position[0]
		self.rect.top = position[1]
		self.active = True