class Settings:
	def __init__(self):
		"""Initialize static settings."""
		# Screen settings.
		self.screen_width = 1200
		self.screen_height = 800
		# Colors
		self.dark_blue = (0, 30, 45)
		self.dark_red = (204, 0, 0)
		# Background color
		self.bg_color = self.dark_blue

		# Laser settings
		self.laser_width = 17
		self.laser_height = 3
		self.laser_color = self.dark_red
		self.lasers_allowed = 3

		# Max nr of available saucers
		self.saucer_limit = 3

		# Speed-up scale
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change as game goes on."""
		# Speed for saucer movement.
		self.saucer_speed = 2.5
		# Laser speed
		self.laser_speed = 3.5
		# Asteroid speed
		self.asteroid_speed = 0.5

	def increase_speed(self):
		self.saucer_speed *= self.speedup_scale
		self.laser_speed *= self.speedup_scale
		self.asteroid_speed *= self.speedup_scale



