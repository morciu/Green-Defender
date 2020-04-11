import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from button import Button

from saucer import Saucer
from laser import Laser
from asteroid import Asteroid

from random import randint

class GreenDefender:
	"""Main class for the game."""
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.stats = GameStats(self)

		self.screen = pygame.display.set_mode(
			(0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		self.saucer = Saucer(self)
		self.lasers = pygame.sprite.Group()
		self.asteroids = pygame.sprite.Group()

		self._create_group_asteroids()

		# Make play button
		self.play_button = Button(self, "Play")

		pygame.display.set_caption("Green Defender")

	def run_game(self):
		"""Main loop."""
		while True:
			self._check_events()
			if self.stats.game_active:
				self.saucer.update()
				self._update_lasers()
				self._update_asteroids()
			self._update_screen()

	def _update_lasers(self):
		"""Update position of the lasers."""
		self.lasers.update()
		# Getting rid of old lasers.
		for laser in self.lasers.copy():
			if laser.rect.left > self.saucer.screen_rect.right:
				self.lasers.remove(laser)
		# Check if any lasers have hit asteroids, and get rid of respective lasers and asteroids.
		collisions = pygame.sprite.groupcollide(
			self.lasers, self.asteroids, True, True)
		if not self.asteroids:
			self.lasers.empty()
			self._create_group_asteroids()

	def _update_asteroids(self):
		for asteroid in self.asteroids.sprites():
			asteroid.rect.x -= self.settings.asteroid_speed
		# React when asteroids hit flying saucer
		if pygame.sprite.spritecollideany(self.saucer, self.asteroids):
			self._player_hit()
		# React when asteroids reach the left edge
		self._check_asteroid_left()

	def _player_hit(self):
		"""Respont to saucer-asteroid collision events."""
		if self.stats.saucers_left > 0:
			# Decrease available saucers.
			self.stats.saucers_left -=1

			# Free up the screen and repopulate it.
			self.asteroids.empty()
			self.lasers.empty()

			# Create a new group of asteroids and re-center the player
			self._create_group_asteroids()
			self.saucer.center_saucer()
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

		#Pause
		sleep(1.0)

	def _check_asteroid_left(self):
		"""Check if any asteroids reach the left edge of the screen."""
		screen_rect = self.screen.get_rect()
		for asteroid in self.asteroids.sprites():
			if asteroid.rect.left <= screen_rect.left:
				self._player_hit()
				break

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		play_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if play_clicked and not self.stats.game_active:
			self._start_game()
			# Hide cursor
			pygame.mouse.set_visible(False)

	def _start_game(self):
		# Reset stats
		self.stats.reset_stats()
		# Activate game
		self.stats.game_active = True
		# Clear screen of remaining asteroids and lasers
		self.asteroids.empty()
		self.lasers.empty()
		# Create new asteroi group and center saucer
		self._create_group_asteroids()
		self.saucer.center_saucer()

	def _check_keydown_events(self, event):
		if event.key == pygame.K_ESCAPE:
			sys.exit()
		if event.key == pygame.K_UP:
			self.saucer.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.saucer.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_laser()

	def _check_keyup_events(self,event):
		if event.key == pygame.K_UP:
			self.saucer.moving_up = False
		if event.key == pygame.K_DOWN:
			self.saucer.moving_down = False

	def _create_group_asteroids(self):
		"""Create a group of asteroids."""
		# Determine available space and the spacing between asteroids.
		asteroid = Asteroid(self)
		saucer_width = self.saucer.rect.width
		asteroid_width, asteroid_height = asteroid.rect.size
		# Determine available space and nr of asteroids in one collumn
		available_space_y = self.settings.screen_height
		number_asteroids_y = available_space_y // asteroid_height
		# Determine available space and nr. of asteroids in one row
		available_space_x = self.settings.screen_width
		number_collumns = available_space_x // (2 * asteroid_width) 
		# Create full group of asteroids
		for collumn_number in range(3, number_collumns):
			for asteroid_number in range(number_asteroids_y):
				self._create_asteroid(asteroid_number, collumn_number)

	def _create_asteroid(self, asteroid_number, collumn_number):
	# Create asteroid and place it in the collumn.
		asteroid = Asteroid(self)
		saucer_width = self.saucer.rect.width
		asteroid_width, asteroid_height = asteroid.rect.size
		asteroid.y = asteroid_height * randint(0, asteroid_number)
		asteroid.rect.y = asteroid.y
		asteroid.rect.x = asteroid.rect.width + 2 * asteroid.rect.width * collumn_number
		self.asteroids.add(asteroid)

	def _fire_laser(self):
		"""Create a new laser and add it to the laser group."""
		new_laser = Laser(self)
		self.lasers.add(new_laser)

	def _update_screen(self):
		# Fills screen with background color
		self.screen.fill(self.settings.bg_color)
		# Draw saucer.
		self.saucer.blitme()
		# Update lasers.
		for laser in self.lasers.sprites():
			laser.draw_laser()
		self.asteroids.draw(self.screen)

		# Draw the play button on screen in game inactive
		if not self.stats.game_active:
			self.play_button.draw_button()
		# Refresh screen
		pygame.display.flip()

if __name__ == '__main__':
	# Make game instance and run the game.
	gf = GreenDefender()
	gf.run_game()

