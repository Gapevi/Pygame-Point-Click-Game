import pygame

from Inventory import PlayerInventory

import utils.colors as colors
from utils.fonts import font, small_font

# TODO:
# Modify is_hovered from objs

class Player:

	def __init__(self):
		self.Inventory = PlayerInventory()
		self.mouse_pos = (0, 0)

	def ready(self):
		pass

	def update(self):

		self.mouse_pos = pygame.mouse.get_pos()

		self.adjusted_mouse_pos = self.camera.update(self.mouse_pos)

	# TODO: Maybe there's a better way to get hovered_obj
	def update_text(self, text_surface, hovered_obj=None):
		if hovered_obj:
			cursor_text = small_font.render(f"{hovered_obj.description}", True, colors.WHITE)
			text_surface.blit(cursor_text, (self.adjusted_mouse_pos[0] + 15, self.adjusted_mouse_pos[1] + 15))

	def set_camera(self, camera): self.camera = camera

	def get_mouse_pos(self): return self.adjusted_mouse_pos
	def get_unadjusted_mouse_pos(self): return self.mouse_pos