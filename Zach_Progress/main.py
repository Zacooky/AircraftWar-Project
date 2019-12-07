'''
This main.py is the code to run the AircraftWar Game!

The images, game music and font are accessible via https://fishc.com.cn/
'''
import pygame
import sys
import traceback
from pygame.locals import *
from random import *
import myplane
import enemy
import bullet
import supply

# We use pygame package to achieve most of the game function.
# So here we need to init the parameter.
pygame.init()
pygame.mixer.init()
# bg_size is the background size of the game
bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('Aircraft_War')

background = pygame.image.load('images/background.png').convert()

# Define Colors
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

# load game music
pygame.mixer.music.load('sound/game_music.wav')
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound('sound/bullet.wav')
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound('sound/use_bomb.wav')
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound('sound/supply.wav')
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound('sound/get_bomb.wav')
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound('sound/get_bullet.wav')
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound('sound/upgrade.wav')
upgrade_sound.set_volume(0.2)
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

def increase_speed(target,inc):
	for each in target:
		each.speed += inc


def main():
	'''
	This main function is to run the game.

	The main function can be divide into two parts. 
	
	In the first part, we defines all the necessary parameters, states(True or False) and index.
	
	In the second part, we use the classes, functions from main.py file and other imported py file to run the game.
	'''


	# THE FIRST PART STARTS HERE!


	pygame.mixer.music.play(-1)

	# Define my hero plane class
	hero = myplane.MyPlane(bg_size)
	# Define small, mid and big enemy planes classes
	enemies = pygame.sprite.Group()
	small_enemies = pygame.sprite.Group()
	add_small_enemies(small_enemies, enemies, 15)
	mid_enemies = pygame.sprite.Group()
	add_mid_enemies(mid_enemies, enemies, 4)
	big_enemies = pygame.sprite.Group()
	add_big_enemies(big_enemies, enemies, 2)

	clock = pygame.time.Clock()

	# Define bullet1 class
	bullet1 = []
	bullet1_index = 0
	bullet1_num = 5
	for i in range(bullet1_num):
		bullet1.append(bullet.Bullet1(hero.rect.midtop))

	# Define super bullet2 class
	bullet2 = []
	bullet2_index = 0
	bullet2_num = 10
	for i in range(bullet2_num // 2):
		bullet2.append(bullet.Bullet2((hero.rect.centerx - 32, hero.rect.centery)))
		bullet2.append(bullet.Bullet2((hero.rect.centerx + 32, hero.rect.centery)))

	# Init Plane destroy images index
	e1_destroy_index = 0
	e2_destroy_index = 0
	e3_destroy_index = 0
	hero_destroy_index = 0

	# Init Score recording
	score = 0
	score_font = pygame.font.Font('Font/font.ttf', 36)

	# Init the pause function
	paused = False
	pause_nor_image = pygame.image.load('images/game_pause_nor.png').convert_alpha()
	pause_pressed_image = pygame.image.load('images/game_pause_pressed.png').convert_alpha()
	resume_nor_image = pygame.image.load('images/game_resume_nor.png').convert_alpha()
	resume_pressed_image = pygame.image.load('images/game_resume_pressed.png').convert_alpha()
	paused_rect = pause_nor_image.get_rect()
	paused_rect.left = width - paused_rect.width - 10
	paused_rect.top = 10
	paused_image = pause_nor_image

	# Init Game Levels
	level = 1

	# Show bomb botton on the game interface
	bomb_image = pygame.image.load('images/bomb.png').convert_alpha()
	bomb_rect = bomb_image.get_rect()
	bomb_font = pygame.font.Font('Font/font.ttf', 48)
	bomb_num = 3

	# Init bullet and bomb supply
	bullet_supply = supply.BulletSupply(bg_size)
	bomb_supply = supply.BombSupply(bg_size)
	supply_time = USEREVENT
	pygame.time.set_timer(supply_time, 5 * 1000)

	# Set bullet supply timer
	super_bullet_time = USEREVENT + 1
	is_super_bullet = False

	# Set Safe timer
	safe_time = USEREVENT + 2

	# Set hero life
	life_image = pygame.image.load('images/life.png').convert_alpha()
	life_rect = life_image.get_rect()
	life_number = 3

	# Init score record 
	recorded = False
	# Init Game Over Screen
	gameover_font = pygame.font.Font('Font/font.TTF', 48)
	restart_image = pygame.image.load('images/restart.png').convert_alpha()
	restart_rect = restart_image.get_rect()
	end_game_image = pygame.image.load('images/end_game.png').convert_alpha()
	end_game_rect = end_game_image.get_rect()

	# Init switch between images
	switch_image = True

	# Set image switch delay
	delay = 100

	# Set  the game running state
	running = True


	# THE SECOND PART!


	while running:
		for event in pygame.event.get():
			# Function: Quit the game 
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			# Function: Pause or Restart the game. When pausing the game, stop playing all the music. 
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1 and paused_rect.collidepoint(event.pos):
					paused = not paused
					if paused:
						pygame.time.set_timer(supply_time, 0)
						pygame.mixer.music.pause()
						pygame.mixer.pause()
					else:
						pygame.time.set_timer(supply_time, 45 * 1000)
						pygame.mixer.music.unpause()
						pygame.mixer.unpause()
			# Function: Show the images of the pause botton. When the mouse move to the pause images, 
			# it will switch another images with deeper color to indicate the gameplayer to press the button.
			elif event.type == MOUSEMOTION:
				if paused_rect.collidepoint(event.pos):
					if paused:
						paused_image = resume_pressed_image
					else:
						paused_image = pause_pressed_image
				else:
					if paused:
						paused_image = resume_nor_image
					else:
						paused_image = pause_nor_image
			# Function: Use the bomb when the gameplayer presses the space key.
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					if bomb_num:
						bomb_num -= 1
						bomb_sound.play()
						for each in enemies:
							if each.rect.bottom > 0:
								each.active = False
			# Function: drop the supply every supply_time(5s).
			# The supply can be bomb or super bullet.
			elif event.type == supply_time:
				supply_sound.play()
				if choice([True, False]):
					bomb_supply.reset()
				else:
					bullet_supply.reset()
			# Function: set the super bullet time
			elif event.type == super_bullet_time:
				is_super_bullet = False
				pygame.time.set_timer(super_bullet_time, 0)
			# Function: set the hero safe time
			elif event.type == safe_time:
				hero.safe = False
				pygame.time.set_timer(safe_time, 0)

		# Enemy level upgrade with score
		if level == 1 and score in range(5000, 50000):
			level = 2
			upgrade_sound.play()
			# Add four small enemies, 2 mid enemies, and 1 big enemy
			add_small_enemies(small_enemies, enemies, 4)
			add_mid_enemies(mid_enemies, enemies, 2)
			add_big_enemies(big_enemies, enemies, 1)
			# Increase the speed of small enemies
			increase_speed(small_enemies, 1)
		elif level == 2 and score in range(50000, 500000):
			level = 3
			upgrade_sound.play()
			# Add four small enemies, 2 mid enemies, and 1 big enemy
			add_small_enemies(small_enemies, enemies, 6)
			add_mid_enemies(mid_enemies, enemies, 3)
			add_big_enemies(big_enemies, enemies, 2)
			# Increase the speed of small enemies
			increase_speed(small_enemies, 1)
			increase_speed(mid_enemies, 1)
		elif level == 3 and score in range(500000, 1000000):
			level = 4
			upgrade_sound.play()
			# Add four small enemies, 2 mid enemies, and 1 big enemy
			add_small_enemies(small_enemies, enemies, 6)
			add_mid_enemies(mid_enemies, enemies, 3)
			add_big_enemies(big_enemies, enemies, 2)
			# Increase the speed of small enemies
			increase_speed(small_enemies, 1)
			increase_speed(mid_enemies, 1)

		# Put background on the game interface
		screen.blit(background, (0, 0))

		# Run the game when not pausing the game and hero plane still alive.
		if not paused and life_number:
			# Detect trace of the keyboard.
			key_pressed = pygame.key.get_pressed()

			if key_pressed[K_w] or key_pressed[K_UP]:
				hero.moveUp()
			if key_pressed[K_s] or key_pressed[K_DOWN]:
				hero.moveDown()
			if key_pressed[K_a] or key_pressed[K_LEFT]:
				hero.moveLeft()
			if key_pressed[K_d] or key_pressed[K_RIGHT]:
				hero.moveRight()

			# Show bomb supply on the game interface
			if bomb_supply.active:
				bomb_supply.move()
				screen.blit(bomb_supply.image, bomb_supply.rect)
				if pygame.sprite.collide_mask(bomb_supply, hero):
					get_bomb_sound.play()
					if bomb_num < 3:
						bomb_num += 1
					bomb_supply.active = False

			# Show bullet supply on the game interface
			if bullet_supply.active:
				bullet_supply.move()
				screen.blit(bullet_supply.image, bullet_supply.rect)
				if pygame.sprite.collide_mask(bullet_supply, hero):
					get_bullet_sound.play()
					# Shoot two bullet
					is_super_bullet = True
					pygame.time.set_timer(super_bullet_time, 20 * 1000)
					bullet_supply.active = False

			# Judge whether the hero plane is using bullet1 or bullet2
			if not(delay % 10):
				bullet_sound.play()
				if is_super_bullet:
					bullets = bullet2
					bullets[bullet2_index].reset((hero.rect.centerx - 32, hero.rect.centery))
					bullets[bullet2_index + 1].reset((hero.rect.centerx + 32, hero.rect.centery))
					bullet2_index = (bullet2_index + 2) % bullet2_num
				else:
					bullets = bullet1
					bullets[bullet1_index].reset(hero.rect.midtop)
					bullet1_index = (bullet1_index + 1) % bullet1_num

			# Show the hero plane's bullet on the game interface
			for b in bullets:
				if b.active:
					b.move()
					screen.blit(b.image, b.rect)
					# Bullet collide detection
					enemy_hit = pygame.sprite.spritecollide(\
						b, enemies, False, pygame.sprite.collide_mask)
					if enemy_hit:
						b.active = False
						for e in enemy_hit:
							# for mid and big enemies, hero plane needs more bullets to kill them
							if e in mid_enemies or e in big_enemies:
								e.hit = True
								e.energy -= 1
								if e.energy == 0:
									e.active = False
							else:
								e.active = False

			# Generate and show enemyPlanes on the game interface
			# Big enemies
			for each in big_enemies:
				if each.active:
					each.move()
					if each.hit:
						# Show hit images
						screen.blit(each.image_hit, each.rect)
						each.hit = False
					elif switch_image:
						screen.blit(each.image1, each.rect)
					else:
						screen.blit(each.image2, each.rect)

					# Showing enemy's remained energy
					pygame.draw.line(screen, BLACK, \
									(each.rect.left, each.rect.top - 5), \
									(each.rect.right, each.rect.top -5), 2,\
									)

					# Show GREEN when enemy energy is greater than 20%, else show RED
					energy_remained = each.energy / enemy.BigEnemy.energy
					if energy_remained > 0.2:
						energy_color = GREEN
					else:
						energy_color = RED
					pygame.draw.line(screen, energy_color, \
									(each.rect.left, each.rect.top - 5), \
									(each.rect.left + each.rect.width * energy_remained, \
									each.rect.top - 5), 2)

					# Play special BGM when big enemy showing up
					if each.rect.bottom == -50:
						enemy3_fly_sound.play(-1)
				else:
					# Destroy big enemy
					if not(delay % 3):
						if e3_destroy_index == 0:
							enemy3_down_sound.play()
						# Show destroyed images
						screen.blit(each.destroy_images[e3_destroy_index], each.rect)
						e3_destroy_index = (e3_destroy_index + 1) % 6
						if e3_destroy_index == 0:
							enemy3_fly_sound.stop()
							score += 10000
							each.reset()

			# Mid enemies
			for each in mid_enemies:
				if each.active:
					each.move()
					if each.hit:
						# Show hit images
						screen.blit(each.image_hit, each.rect)
						each.hit = False
					else:
						screen.blit(each.image, each.rect)

					# Showing enemy's remained energy
					pygame.draw.line(screen, BLACK, \
									(each.rect.left, each.rect.top - 5), \
									(each.rect.right, each.rect.top -5), 2,\
									)

					# Show GREEN when enemy energy is greater than 20%, else show RED
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
					# Destroy mid enemy
					if not(delay % 3):
						if e2_destroy_index == 0:
							enemy2_down_sound.play()
						# Show destroyed images
						screen.blit(each.destroy_images[e2_destroy_index], each.rect)
						e2_destroy_index = (e2_destroy_index + 1) % 4
						if e2_destroy_index == 0:
							score += 6000
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
							score += 1000
							each.reset()

			# Collide detection between hero plane and enemy
			enemies_down = pygame.sprite.spritecollide(hero, enemies, False, pygame.sprite.collide_mask)
			if enemies_down and not hero.safe:
				hero.active = False
				for e in enemies_down:
					e.active = False

			# Generate and show my hero plane on the game interface
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
						life_number -= 1
						hero.reset()
						pygame.time.set_timer(safe_time, 3 * 1000)

			# Show bomb remaining image on the game interface
			bomb_text = bomb_font.render('X %d' % bomb_num, True, WHITE)
			text_rect = bomb_text.get_rect()
			screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
			screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))

			# Show remaining life of the hero plane on the game interface
			if life_number:
			 	for i in range(life_number):
			 		screen.blit(life_image, (width - 10 - (i+1)* life_rect.width,\
			 			height - 10 - life_rect.height))

		# Game Over Set up
		elif life_number == 0:
			# Stop BGM
			pygame.mixer.music.stop()
			pygame.mixer.stop()
			pygame.time.set_timer(supply_time, 0)

			if not recorded:
				recorded = True

			# Show history highest score
			with open('record.txt', 'r') as f:
				record_score = int(f.read())
			if score > record_score:
				with open('record.txt', 'w') as f:
					f.write(str(score))

			# Show Gamve Over Screen
			recorded_score_txt = score_font.render('Highest: %d' % record_score, True, WHITE)
			screen.blit(recorded_score_txt, (52, 52))

			gameover_txt1 = gameover_font.render('Your Score is: ', True, WHITE)
			gameover_txt1_rect = gameover_txt1.get_rect()
			gameover_txt1_rect.left = (width - gameover_txt1_rect.width) // 2
			gameover_txt1_rect.top = height // 2
			screen.blit(gameover_txt1, gameover_txt1_rect)

			gameover_txt2 = gameover_font.render(str(score), True, WHITE)
			gameover_txt2_rect = gameover_txt2.get_rect()
			gameover_txt2_rect.left = (width - gameover_txt2_rect.width) // 2
			gameover_txt2_rect.top = gameover_txt1_rect.bottom + 10
			screen.blit(gameover_txt2, gameover_txt2_rect)

			restart_rect.left = (width - restart_rect.width) // 2
			restart_rect.bottom = gameover_txt2_rect.bottom + 50
			screen.blit(restart_image, restart_rect)

			end_game_rect.left = (width - restart_rect.width) // 2
			end_game_rect.top = restart_rect.bottom + 10
			screen.blit(end_game_image, end_game_rect)

			if pygame.mouse.get_pressed()[0]:
				position = pygame.mouse.get_pos()
				if restart_rect.left < position[0] < restart_rect.right and \
				restart_rect.top < position[1] < restart_rect.bottom:
					main()
				elif end_game_rect.left < position[0] < end_game_rect.right and \
				end_game_rect.top < position[1] < end_game_rect.bottom:
					pygame.quit()
					sys.exit()

		# Show score on game screen
		score_text = score_font.render('Score: %s' % str(score), True, WHITE)
		screen.blit(score_text, (10, 5))

		# Show pause button
		screen.blit(paused_image, paused_rect)

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
