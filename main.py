import pygame
import sys
import traceback
from pygame.locals import *
import myplane
import enemy


pygame.init()
pygame.mixer.init()

bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('AirFightDemo')

background = pygame.image.load('images/background.png').convert()

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






def add_small_enemies(group1, group2, num):
	for i in range(num):
		e1 = enemy.SmallEnemy(bg_size)
		group1.add(e1)
		group2.add(e1)

def add_mid_enemies(group1, group2, num):
	for i in range(num):
		e2 = enemy.MidEnemy(bg_size)
		group1.add(e2)
		group2.add(e2)

def add_big_enemies(group1, group2, num):
	for i in range(num):
		e3 = enemy.BigEnemy(bg_size)
		group1.add(e3)
		group2.add(e3)


def main(): 
	pygame.mixer.music.play(-1)

	# 生成我方飞机
	hero = myplane.Myplane(bg_size)

	# 生成敌方飞机
	enemies = pygame.sprite.Group()
	# 生成小飞机
	small_enemies = pygame.sprite.Group()
	add_small_enemies(small_enemies, enemies, 15)
	# 生成中飞机
	mid_enemies = pygame.sprite.Group()
	add_mid_enemies(mid_enemies, enemies, 4)
	# 生成大飞机
	big_enemies = pygame.sprite.Group()
	add_big_enemies(big_enemies, enemies, 4)

	clock = pygame.time.Clock()

	# 中弹图片索引
	e1_destroy_index = 0
	e2_destroy_index = 0
	e3_destroy_index = 0
	hero_destroy_index = 0


	# 用于切换图片
	switch_image = True

	# 用于延迟
	delay = 100

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


		# 检测用户的键盘操作
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

		# generate big enemies
		for each in big_enemies:
			# if the big enemy is active:
			if each.active:
				each.move()
				# show the two images of the big enemy
				if switch_image:
					screen.blit(each.image1, each.rect)
				else:
					screen.blit(each.image2, each.rect)
				# play the sound of the big enemy
				if each.rect.bottom > -50:
					enemy3_fly_sound.play(-1)
			# if the big enemy is destroyed		
			else:
				if not(delay % 3):
					# play the destroyed sound of the big enemy
					if e3_destroy_index == 0:
						enemy3_down_sound.play()
					# show the six destroyed images of the big enemy
					screen.blit(each.destroy_images[e3_destroy_index], each.rect)
					e3_destroy_index = (e3_destroy_index + 1) % 6 # the index number can only be 1,2,3,4,5,0
					if e3_destroy_index == 0:
						# hero_down_sound.stop()
						each.reset()


		# generate mid enemies
		for each in mid_enemies:
			# if the mid enemy is active:			
			if each.active:
				each.move()
				# show the image of the mid enemy
				screen.blit(each.image, each.rect)
			# if the mid enemy is destroyed:			
			else:
				if not(delay % 3):
					# play the destroyed sound of the mid enemy
					if e2_destroy_index == 0:
						enemy2_down_sound.play()
					# show the four destroyed images of the mid enemy
					screen.blit(each.destroy_images[e2_destroy_index], each.rect)
					e2_destroy_index = (e2_destroy_index + 1) % 4 # the index number can only be 1,2,3,0
					if e2_destroy_index == 0:
						each.reset()



		# generate small enemies
		for each in small_enemies:
			# if the small enemy is active:
			if each.active:
				each.move()
				# show the image of the small enemy
				screen.blit(each.image, each.rect)
			# if the small enemy is destroyed
			else:
				if not(delay % 3):
					if e1_destroy_index == 0:
					# play the destroyed sound of the small enemy
						enemy1_down_sound.play()
					# show the four destroyed images of the small enemy
					screen.blit(each.destroy_images[e1_destroy_index], each.rect)
					e1_destroy_index = (e1_destroy_index + 1) % 4 # the index number can only be 1,2,3,0
					if e1_destroy_index == 0:
						each.reset()

		# 检测我方飞机是否被撞
		enemies_down = pygame.sprite.spritecollide(hero, enemies, False, pygame.sprite.collide_mask)
		if enemies_down:
			hero.active = False
			for e in enemies_down:
				e.active = False

	

		# generate my hero plane
		switch_image = not switch_image
		# if the hero plane is active:
		if hero.active:
			if switch_image:
				screen.blit(hero.image1, hero.rect)
			else:
				screen.blit(hero.image2, hero.rect)
		# if the hero plane is destroyed
		else:
			# show the four destroyed images of the hero plane
			if not(delay % 3):
				screen.blit(each.destroy_images[hero_destroy_index], hero.rect)
				hero_destroy_index = (hero_destroy_index + 1) % 4 # the index number can only be 1,2,3,0
				if hero_destroy_index == 0:
					# hero.reset()
					print('GAME OVER!')
					running = False



		# 切换图片
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
