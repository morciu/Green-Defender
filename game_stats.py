class GameStats:
	"""Track game statistics."""
	def __init__(self, gf_game):
		"""Initialize statistics."""
		self.settings = gf_game.settings
		self.reset_stats()

		# Start game in an active state.
		self.game_active = False

	def reset_stats(self):
		"""Initialize stats that can change during the game."""
		self.saucers_left = self.settings.saucer_limit
		self.score = 0