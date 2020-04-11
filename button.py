import pygame.font

class Button:
	def __init__(self, gf_game, msg):
		"""Button attributes."""
		self.screen = gf_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (255, 0, 0)
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and center that bitch.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# Prep the button message
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn message into rendered image and center it on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color,
											 self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Draw blank button and then draw the message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
