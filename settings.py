class Settings:
	def __init__(self):
		# Screen settings.
		self.screen_width = 1200
		self.screen_height = 800
		# Colors
		self.dark_blue = (0, 30, 45)
		self.dark_red = (204, 0, 0)
		# Background color
		self.bg_color = self.dark_blue
		# Set speed for saucer movement.
		self.saucer_speed = 2.5

		# Laser settings
		self.laser_speed = 3.5
		self.laser_width = 17
		self.laser_height = 3
		self.laser_color = self.dark_red

		# Asteroid settings
		self.asteroid_speed = 0.5

		# Max nr of available saucers
		self.saucer_limit = 3