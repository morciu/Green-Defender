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

		# Prepare score images
		self.prep_score()
		self.prep_high_score()
		self.prep_stage()

	def prep_stage(self):
		"""Turn stage info into a rendered image."""
		stage_str = str(self.stats.stage)
		self.stage_image = self.font.render(stage_str, True, 
			self.text_color, self.settings.bg_color)

		# Place stage image bottom center of screen
		self.stage_rect = self.stage_image.get_rect()
		self.stage_rect.centerx = self.screen_rect.centerx
		self.stage_rect.bottom = self.screen_rect.bottom

	def prep_high_score(self):
		"""Turn high score info into a rendered image."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, 
			self.text_color, self.settings.bg_color)

		# Position the high score bottom right
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.right = self.screen_rect.right - 20
		self.high_score_rect.bottom = self.screen_rect.bottom - 20

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
		"""Draw score and stage nr to te screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.stage_image, self.stage_rect)

	def check_high_score(self):
		"""Check if there is a new high score."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()
