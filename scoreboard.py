import pygame.font
from pygame.sprite import Group

from saucer import Saucer

class Scoreboard:
	"""A class for the scoreboard."""

	def __init__(self, gf_game):
		"""Initialize scorekeeping attributes."""
		self.gf_game = gf_game
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
		self.prep_saucers()

	def prep_saucers(self):
		"""Show how many flying saucers are left."""
		self.saucers = Group()
		for saucer_nr in range(self.stats.saucers_left):
			saucer = Saucer(self.gf_game)
			saucer.rect.width = int(saucer.rect.width / 4)
			saucer.rect.height = int(saucer.rect.height / 4)
			saucer.image = pygame.transform.scale(saucer.image, (saucer.rect.width, saucer.rect.height))
			saucer.rect.left = 10 + (saucer_nr * saucer.rect.width)
			saucer.rect.bottom = self.score_rect.top
			self.saucers.add(saucer)

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
		"""Draw score, stage nr and lives left to te screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.stage_image, self.stage_rect)
		self.saucers.draw(self.screen)

	def check_high_score(self):
		"""Check if there is a new high score."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()
