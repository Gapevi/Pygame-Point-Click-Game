from abc import ABC, abstractmethod
import pygame
import Events
import utils.sounds as sounds
from utils.resource_path import resource_path 
from .InteractableArea import BaseInteractableArea

"""
Class for InteractableSprites

Contructor:
	name: 			str = Name of the Sprite 
	description:	str = Description of the Sprite
	image_path: 	str = Path for the sprite image
	group: 			str = Sprite group
	position: 		str = Sprite initial position
	**kwargs 			= View BaseInteractableArea
"""

class BaseInteractableSprite(BaseInteractableArea, pygame.sprite.Sprite, ABC):
	def __init__(self, name, description, image_path, group, position=(0, 0), **kwargs):
		pygame.sprite.Sprite.__init__(self, group)

		# Testing Logic
		self.name=name
		self.description=description
		self.image_path=image_path
		self.position=position
		self._kwargs=kwargs

		self._initialized=False

		#self.image = pygame.image.load(resource_path(image_path)).convert()
		#self.rect = self.image.get_rect()
		#self.rect.topleft = position
		#BaseInteractableArea.__init__(self, self.rect, name, description, **kwargs)
		#self.image.set_alpha(self.transparency)  

	def ready(self, surface):
		if self._initialized: return

		self.surface = surface

		self.image = pygame.image.load(resource_path(self.image_path)).convert()

		self.rect = self.image.get_rect()
		self.rect.topleft = self.position
		BaseInteractableArea.__init__(self, self.rect, self.name, self.description, **self._kwargs)

		self.image.set_alpha(self.transparency)

		self._initialized=True  

	@abstractmethod
	def on_clicked(self): pass
	@abstractmethod
	def interact(self): return self.event

	def draw(self, surface):
		surface.blit(self.image, self.rect)

class TestInteractableSprite(BaseInteractableSprite):
	def __init__(self, name, image, description, group, position=(0,0), **kwargs):
		super().__init__(name, image, description, group, position, **kwargs)

	def interact(self):
		sounds.play_swoosh()
		return self.event

	def on_clicked(self):
		sounds.play_punch()

class InteractableSprite(BaseInteractableSprite):
	def __init__(self, name, image, description, group, position=(0,0), **kwargs):
		super().__init__(name, image, description, group, position, **kwargs)

	def interact(self): return self.event

	def on_clicked(self): pass
