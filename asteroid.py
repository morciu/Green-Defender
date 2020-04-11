import pygame
from pygame.sprite import Sprite
from settings import Settings

class Asteroid(Sprite):
	"""A class to represent a single asteroid in the asteroid group."""
	def __init__(self, gf_game):
		"""Initialize asteroid and set its starting position."""
		super().__init__()
		self.screen = gf_game.screen
		self.settings = gf_game.settings
		self.screen_rect = gf_game.screen.get_rect()

		# Load the asteroid and set its rect attribute.
		self.image = pygame.image.load('images/asteroid.png')
		self.rect = self.image.get_rect()
		self.rect_height_half = self.rect.height / 2

		# Start each new asteroid at the right side of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the asteroid's exact horizontal position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""Move asteroid foward."""
		self.x -= self.settings.asteroid_speed
		self.rect.x = self.x
