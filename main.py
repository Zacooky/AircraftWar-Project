import pygame
import sys
import traceback
from pygame.locals import *
from random import *
import myplane
import enemy
import bullet

pygame.init()
pygame.mixer.init()

bg_size = width, height = 480,700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('Aircraft_War_Demo')

background = pygame.image.load('images/background.png').convert()

# Define Colors
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)


# load game music
pygame.mixer.music.load('sound/game_music.wav')
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound('sound/bullet.wav')
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound('sound/use_bomb.wav')
bomb_sound.set_volume(0.2)
# supply_sound = pygame.mixer.Sound('sound/supply.wav')
# supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound('sound/get_bomb.wav')
get_bomb_sound.set_volume(0.2)
# get_bullet_sound = pygame.mixer.Sound('sound/get_bullet.wav')
# get_bullet_sound.set_volume(0.2)
# upgrade_sound = pygame.mixer.Sound('sound/upgrade.wav')
# upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound('sound/enemy3_flying.wav')
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound('sound/enemy1_down.wav')
enemy1_down_sound.set_volume(0.1)
enemy2_down_sound = pygame.mixer.Sound('sound/enemy2_down.wav')
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound('sound/enemy3_down.wav')
enemy3_down_sound.set_volume(0.5)
hero_down_sound = pygame.mixer.Sound('sound/hero_down.wav')
hero_down_sound.set_volume(0.2)

def add_small_enemies(group1,group2,num):
	for i in range(num):
		e1 = enemy.SmallEnemy(bg_size)
		group1.add(e1)
		group2.add(e1)

def add_mid_enemies(group1,group2,num):
	for i in range(num):
		e2 = enemy.MidEnemy(bg_size)
		group1.add(e2)
		group2.add(e2)

def add_big_enemies(group1,group2,num):
	for i in range(num):
		e3 = enemy.BigEnemy(bg_size)
		group1.add(e3)
		group2.add(e3)



def main():
	pygame.mixer.music.play(-1)

	# Define myPlane
	hero = myplane.MyPlane(bg_size)
	# Define enemyPlanes
	enemies = pygame.sprite.Group()
	small_enemies = pygame.sprite.Group()
	add_small_enemies(small_enemies, enemies, 15)
	mid_enemies = pygame.sprite.Group()
	add_mid_enemies(mid_enemies, enemies, 4)
	big_enemies = pygame.sprite.Group()
	add_big_enemies(big_enemies, enemies, 2)

	clock = pygame.time.Clock()

	# Define bullet
	bullet1 = []
	bullet1_index = 0
	bullet1_num = 5
	for i in range(bullet1_num):
		bullet1.append(bullet.Bullet1(hero.rect.midtop))


	# Plane destroy images index
	e1_destroy_index = 0
	e2_destroy_index = 0
	e3_destroy_index = 0
	hero_destroy_index = 0

	# myPlan switch between images
	switch_image = True

	# image switch delay
	delay = 100

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		# Detect trace of the mouse.
		key_pressed = pygame.key.get_pressed()

		if key_pressed[K_w] or key_pressed[K_UP]:
			hero.moveUp()
		if key_pressed[K_s] or key_pressed[K_DOWN]:
			hero.moveDown()
		if key_pressed[K_a] or key_pressed[K_LEFT]:
			hero.moveLeft()
		if key_pressed[K_d] or key_pressed[K_RIGHT]:
			hero.moveRight()

		screen.blit(background, (0, 0))

		# Bullet fire
		if not(delay % 10):
			bullet1[bullet1_index].reset(hero.rect.midtop)
			bullet1_index = (bullet1_index + 1) % bullet1_num

		# Bullet collide detection
		for b in bullet1:
			if b.active:
				b.move()
				screen.blit(b.image, b.rect)
				enemy_hit = pygame.sprite.spritecollide(\
					b, enemies, False, pygame.sprite.collide_mask)
				if enemy_hit:
					b.active = False
					for e in enemy_hit:
						if e in mid_enemies or e in big_enemies:
							e.hit = True
							e.energy -= 1
							if e.energy == 0:
								e.active = False
						else:
							e.active = False




		# Generate enemyPlanes
		# Big enemies
		for each in big_enemies:
			if each.active:
				each.move()
				if each.hit:
					# Show hit special effect
					screen.blit(each.image_hit, each.rect)
					each.hit = False
				elif switch_image:
					screen.blit(each.image1, each.rect)
				else:
					screen.blit(each.image2, each.rect)

				# Showing energy remained
				pygame.draw.line(screen, BLACK, \
								(each.rect.left, each.rect.top - 5), \
								(each.rect.right, each.rect.top -5), 2,\
								)

				# Show GREEN when enemy energy is grater than 20%, else show red
				energy_remained = each.energy / enemy.BigEnemy.energy
				if energy_remained > 0.2:
					energy_color = GREEN
				else:
					energy_color = RED
				pygame.draw.line(screen, energy_color, \
								(each.rect.left, each.rect.top - 5), \
								(each.rect.left + each.rect.width * energy_remained, \
								each.rect.top - 5), 2)

				# Play special BGM when big enemy is showing up
				if each.rect.bottom == -50:
					enemy3_fly_sound.play(-1)
			else:
				# Destroy big enemies
				if not(delay % 3):
					if e3_destroy_index == 0:
						enemy3_down_sound.play()
					screen.blit(each.destroy_images[e3_destroy_index], each.rect)
					e3_destroy_index = (e3_destroy_index + 1) % 6
					if e3_destroy_index == 0:
						enemy3_fly_sound.stop()
						each.reset()


		# Mid enemies
		for each in mid_enemies:
			if each.active:
				each.move()
				if each.hit:
					screen.blit(each.image_hit, each.rect)
					each.hit = False
				else:
					screen.blit(each.image, each.rect)

				# Showing energy remained
				pygame.draw.line(screen, BLACK, \
								(each.rect.left, each.rect.top - 5), \
								(each.rect.right, each.rect.top -5), 2,\
								)

				# Show GREEN when enemy energy is grater than 20%, else show red
				energy_remained = each.energy / enemy.MidEnemy.energy
				if energy_remained > 0.2:
					energy_color = GREEN
				else:
					energy_color = RED
				pygame.draw.line(screen, energy_color, \
								(each.rect.left, each.rect.top - 5), \
								(each.rect.left + each.rect.width * energy_remained, \
								each.rect.top - 5), 2)

			else:
				# Destroy mid enemies
				if not(delay % 3):
					if e2_destroy_index == 0:
						enemy2_down_sound.play()
					screen.blit(each.destroy_images[e2_destroy_index], each.rect)
					e2_destroy_index = (e2_destroy_index + 1) % 4
					if e2_destroy_index == 0:
						each.reset()

		# Small enemies
		for each in small_enemies:
			if each.active:
				each.move()
				screen.blit(each.image, each.rect)
			else:
				# Destroy small enemies
				if not(delay % 3):
					if e1_destroy_index == 0:
						enemy1_down_sound.play()
					screen.blit(each.destroy_images[e1_destroy_index], each.rect)
					e1_destroy_index = (e1_destroy_index + 1) % 4
					if e1_destroy_index == 0:
						each.reset()


		# Collide detection
		enemies_down = pygame.sprite.spritecollide(hero, enemies, False, pygame.sprite.collide_mask)
		if enemies_down:
			hero.active = False
			for e in enemies_down:
				e.active = False

		# Generate myPlane
		if hero.active:
			if switch_image:
				screen.blit(hero.image1, hero.rect)
			else:
				screen.blit(hero.image2, hero.rect)
		else:
			# Destroy hero plane
			if not(delay % 3):
				if hero_destroy_index == 0:
					hero_down_sound.play()
				screen.blit(hero.destroy_images[hero_destroy_index], hero.rect)
				hero_destroy_index = (hero_destroy_index + 1) % 4
				if hero_destroy_index == 0:
					# each.reset()
					print('Game Over!')
					running = False

		# Switch between images with delay
		if not(delay % 5):
			switch_image = not switch_image

		delay -= 1
		if not delay:
			delay = 100

		pygame.display.flip()

		clock.tick(60)

if __name__ == '__main__':
	try:
		main()
	except SystemExit:
		pass
	except:
		traceback.print_exc()
		pygame.quit()
		input()
