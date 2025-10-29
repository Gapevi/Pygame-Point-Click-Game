from abc import ABC, abstractmethod
import pygame
from utils.resource_path import resource_path

from .BaseScene import BaseScene
class Room(BaseScene):
	def __init__(self, name, ID, bg_img_path, objects=[], **kwargs):
		
		super().__init__(ID, name, bg_img_path, objects, **kwargs)

	def load_scene(self, surface):
		self.surface = surface
		self.bg_img = pygame.image.load(resource_path(self.bg_img_path)).convert()
		for obj in self.objects:
			obj.ready(surface)

	def update_scene(self):
		self.surface.blit(self.bg_img, self.bg_img_position)
		for obj in self.objects:
			obj.draw(self.surface)
