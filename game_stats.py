class GameStats:
	"""Track game statistics."""
	def __init__(self, gf_game):
		"""Initialize statistics."""
		self.settings = gf_game.settings
		self.reset_stats()

		# Start game in an active state.
		self.game_active = False

		# High score that should never be reset.
		with open('high_score.txt') as high_score:
			self.high_score = int(high_score.read())

	def reset_stats(self):
		"""Initialize stats that can change during the game."""
		self.saucers_left = self.settings.saucer_limit
		self.score = 0

		# Stage number
		self.stage = 1