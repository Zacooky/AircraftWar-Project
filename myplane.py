'''
This code contains MyPlane class. 

By generate a MyPlane instance(hero plane) in main.py, it can be used to 
generate a hero plane in the game and the gameplayer can control the hero plane 
to move up/down/left/right.

**Functions**	
	__init__:
		init the self parameters of MyPlane instance
	moveUp/moveDown/moveLeft/moveRight:
		control the hero plane to move up/down/left/right.
	reset:
		reset the hero plane
'''

import pygame

class MyPlane(pygame.sprite.Sprite):
	def __init__(self, bg_size):
		pygame.sprite.Sprite.__init__(self)

		self.image1 = pygame.image.load('images/hero1.png').convert_alpha()
		self.image2 = pygame.image.load('images/hero2.png').convert_alpha()
		# Add destroy images of myPlane
		self.destroy_images = []
		self.destroy_images.extend([\
			pygame.image.load('images/hero_blowup_n1.png').convert_alpha(),\
			pygame.image.load('images/hero_blowup_n2.png').convert_alpha(),\
			pygame.image.load('images/hero_blowup_n3.png').convert_alpha(),\
			pygame.image.load('images/hero_blowup_n4.png').convert_alpha()\
			])

		self.rect = self.image1.get_rect()
		self.width = bg_size[0]
		self.height = bg_size[1]
		self.rect.left = (self.width - self.rect.width) // 2
		self.rect.top = self.height - self.rect.height - 50

		self.speed = 10
		self.active = True
		self.safe = False
		self.mask = pygame.mask.from_surface(self.image1)

	def moveUp(self):
		if self.rect.top > 0:
			self.rect.top -= self.speed
		else:
			self.rect.top = 0

	def moveDown(self):
		if self.rect.bottom < self.height - 50:
			self.rect.top += self.speed
		else:
			self.rect.bottom = self.height - 50

	def moveLeft(self):
		if self.rect.left > 0:
			self.rect.left -= self.speed
		else:
			self.rect.left = 0

	def moveRight(self):
		if self.rect.right < self.width:
			self.rect.left += self.speed
		else:
			self.rect.right = self.width

	def reset(self):
		self.rect.left = (self.width - self.rect.width) // 2
		self.rect.top = self.height - self.rect.height - 50
		self.active = True
		self.safe = True
