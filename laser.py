import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
	"""A class to manage lasers fired by flying saucer."""

	def __init__(self, gf_game):
		"""Create laser object at the saucer's current position."""
		super().__init__()
		self.screen = gf_game.screen
		self.settings = gf_game.settings
		self.color = self.settings.laser_color

		# Create a bullet rect at (0, 0) and then correct position.
		self.rect = pygame.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
		self.rect.midright = gf_game.saucer.rect.midright

		# Store the laser's position as a decimal value
		self.x = float(self.rect.x)

	def update(self):
		"""Move the laser horizontaly."""
		# Update decimal position of the laser.
		self.x += self.settings.laser_speed
		# Update rect position
		self.rect.x = self.x

	def draw_laser(self):
		"""Draw the laser to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)