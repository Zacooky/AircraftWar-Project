import pygame
from random import *

class SmallEnermy(pygame.sprite.Sprite):
	def __init__(self, bg_size):
		pygame.sprite.Sprite.__init__(self)		

		self.image = pygame.image.load('images/enemy1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.width, self.height = bg_size[0], bg_size[1]
		self.speed = 2
		self.rect.left, self.rect.top = \
						randint(0, self.width - self.rect.width), \
						randint(-5 * self.height, 0)

	def move(self):
		if self.rect.top < self.height:
			self.rect.top += self.speed
		else:
			self.reset()

	def reset(self):
		self.rect.left, self.rect.top = \
						randint(0, self.width - self.rect.width), \
						randint(-5 * self.height, 0)

class MidEnermy(pygame.sprite.Sprite):
	def __init__(self, bg_size):
		pygame.sprite.Sprite.__init__(self)		

		self.image = pygame.image.load('images/enemy2.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.width, self.height = bg_size[0], bg_size[1]
		self.speed = 1
		self.rect.left, self.rect.top = \
						randint(0, self.width - self.rect.width), \
						randint(-10 * self.height, -self.height)

	def move(self):
		if self.rect.top < self.height:
			self.rect.top += self.speed
		else:
			self.reset()

	def reset(self):
		self.rect.left, self.rect.top = \
						randint(0, self.width - self.rect.width), \
						randint(-10 * self.height, -self.height)

class BigEnermy(pygame.sprite.Sprite):
	def __init__(self, bg_size):
		pygame.sprite.Sprite.__init__(self)		

		self.image1 = pygame.image.load('images/enemy3_n1.png').convert_alpha()
		self.image2 = pygame.image.load('images/enemy3_n2.png').convert_alpha()
		self.rect = self.image1.get_rect()
		self.width, self.height = bg_size[0], bg_size[1]
		self.speed = 1
		self.rect.left, self.rect.top = \
						randint(0, self.width - self.rect.width), \
						randint(-15 * self.height, -5 * self.height)

	def move(self):
		if self.rect.top < self.height:
			self.rect.top += self.speed
		else:
			self.reset()

	def reset(self):
		self.rect.left, self.rect.top = \
						randint(0, self.width - self.rect.width), \
						randint(-15 * self.height, -5 * self.height)

