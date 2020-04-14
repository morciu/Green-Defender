import pygame.font

class Scoreboard:
	"""A class for the scoreboard."""

	def __init__(self, gf_game):
		"""Initialize scorekeeping attributes."""
		self.screen = gf_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = gf_game.settings
		self.stats = gf_game.stats

		# Font settings for score.
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 48)

		# Prepare score image
		self.prep_score()

	def prep_score(self):
		"""Turn score into a rendered image."""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, 
			self.text_color, self.settings.bg_color)

		# Display the score bottom left of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.left = self.screen_rect.left + 20
		self.score_rect.bottom = self.screen_rect.bottom - 20

	def show_score(self):
		"""Draw score to te screen."""
		self.screen.blit(self.score_image, self.score_rect)
