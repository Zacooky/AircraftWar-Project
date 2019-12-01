import pygame
import sys
import traceback
from pygame.locals import *
import myplane
import enermy


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
enermy3_fly_sound = pygame.mixer.Sound('sound/enermy3_flying.wav')
enermy3_fly_sound.set_volume(0.2)
enermy1_down_sound = pygame.mixer.Sound('sound/enermy1_down.wav')
enermy1_down_sound.set_volume(0.1)
enermy2_down_sound = pygame.mixer.Sound('sound/enermy2_down.wav')
enermy2_down_sound.set_volume(0.2)
enermy3_down_sound = pygame.mixer.Sound('sound/enermy3_down.wav')
enermy3_down_sound.set_volume(0.5)






def add_small_enermies(group1, group2, num):
	for i in range(num):
		e1 = enermy.SmallEnermy(bg_size)
		group1.add(e1)
		group2.add(e1)

def add_mid_enermies(group1, group2, num):
	for i in range(num):
		e2 = enermy.MidEnermy(bg_size)
		group1.add(e2)
		group2.add(e2)

def add_big_enermies(group1, group2, num):
	for i in range(num):
		e3 = enermy.BigEnermy(bg_size)
		group1.add(e3)
		group2.add(e3)


def main(): 
	pygame.mixer.music.play(-1)

	# 生成我方飞机
	hero = myplane.Myplane(bg_size)

	# 生成敌方飞机
	enermies = pygame.sprite.Group()
	# 生成小飞机
	small_enermies = pygame.sprite.Group()
	add_small_enermies(small_enermies, enermies, 15)
	# 生成中飞机
	mid_enermies = pygame.sprite.Group()
	add_mid_enermies(mid_enermies, enermies, 4)
	# 生成大飞机
	big_enermies = pygame.sprite.Group()
	add_big_enermies(big_enermies, enermies, 4)



	clock = pygame.time.Clock()

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

		# 绘制大飞机
		for each in big_enermies:
			each.move()
			if switch_image:
				screen.blit(each.image1, each.rect)
			else:
				screen.blit(each.image2, each.rect)
			# 播放大飞机出场音效
			if each.rect.bottom > -50:
				enermy3_fly_sound.play()

		# 绘制中飞机
		for each in mid_enermies:
			each.move()
			screen.blit(each.image, each.rect)

		# 绘制小飞机
		for each in small_enermies:
			each.move()
			screen.blit(each.image, each.rect)
				





		# 绘制我方飞机
		switch_image = not switch_image
		if switch_image:
			screen.blit(hero.image1, hero.rect)
		else:
			screen.blit(hero.image2, hero.rect)


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
