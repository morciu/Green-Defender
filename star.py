import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""Class to manage star sprite."""
	def __init__(self, stars_game):
		super().__init__()
		self.screen = stars_game.screen
		self.settings = stars_game.settings
		self.screen_rect = stars_game.screen.get_rect()

		"""Load star image and GET RECT."""
		self.image = pygame.image.load('images/small_star.png')
		self.rect = self.image.get_rect()

		"""Start each new star at the top left of the screen."""
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		"""Store the star's exact horizontal position."""
		self.x = float(self.rect.x)


