import pygame

class Saucer:
	"""A class to manage flying saucer."""
	def __init__(self, gf_game):
		self.screen = gf_game.screen
		self.settings = gf_game.settings
		self.screen_rect = gf_game.screen.get_rect()

		# Load flying saucer image.
		self.image = pygame.image.load('images/saucer_new.png')
		self.rect = self.image.get_rect()

		# Start each flying saucer at the left center side of the screen.
		self.rect.midleft = self.screen_rect.midleft

		# Store a decimal value for the saucer's vertical position.
		self.y = float(self.rect.y)

		# Movement flag.
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update saucer's position baset on movement flags."""
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.y -= self.settings.saucer_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.saucer_speed

		# Update rect object from self.y
		self.rect.y = self.y

	def blitme(self):
		"""Draw the flying saucer at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_saucer(self):
		"""Re-center the flying saucer after getting hit."""
		self.rect.midleft = self.screen_rect.midleft
		self.y = float(self.rect.y)
