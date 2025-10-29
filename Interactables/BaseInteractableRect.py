import pygame
from abc import ABC, abstractmethod

import utils.colors as colors

from utils.fonts import font, small_font

import utils.sounds as sounds

import Events

from .InteractableArea import BaseInteractableArea

"""
Definition of InteractableArea class

Description:
	Class that creates basic rectangles with interactable properties

Constructor:
	rect:		(x, y, w, h)= Dimensions of the rect (as used by pygame.Rect, i dunno the order)
	name: 			str 	= Name of the Sprite 
	description:	str 	= Description of the Sprite
"""

class BaseInteractableRect(BaseInteractableArea, ABC):

	def __init__(self, rect, name, description, **kwargs):
		BaseInteractableArea.__init__(self, rect, name, description, **kwargs)
		self.color = self.color if self.color != None else colors.BROWN
		self.hovered_color = self.hovered_color if self.hovered_color != None else colors.YELLOW
		
		self.rect = self.area 

	def on_clicked(self): 
		sounds.play_alarm()

	def interact(self):
		sounds.play_blop22()
		return self.event

	def check_hover(self, pos):
		if self.rect.collidepoint(pos):
			self._hover()
		else:
			self._unhover()
		return self.is_hovered

	def draw(self, surface):
		color = self.hovered_color if self.is_hovered else self.color

		if self.transparency != 255:
			# Creates a transparent surface to draw
			temp_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)

			# Draw triangles on the temporary surface at (0, 0)
			pygame.draw.rect(temp_surface, (*color, self.transparency), (0, 0, *self.rect.size))
			pygame.draw.rect(temp_surface, (*colors.BLACK, self.transparency), (0, 0, *self.rect.size), 2)

			surface.blit(temp_surface, self.rect.topleft)
		else:
			pygame.draw.rect(surface, color, self.rect)
			pygame.draw.rect(surface, colors.BLACK, self.rect, 2)

		# Draw name on center if hovered
		if self.is_hovered:
			text = small_font.render(self.name, True, colors.BLACK)
			text_rect = text.get_rect(center=self.rect.center)
			surface.blit(text, text_rect)

class InteractableRect(BaseInteractableRect):

	def __init__(self, rect, name, description, **kwargs):
		super().__init__(rect, name, description, **kwargs)

class TestBaseInteractableRect(BaseInteractableRect):

	def __init__(self, rect, name, description, **kwargs):
		super().__init__(rect, name, description, **kwargs)

	def on_clicked(self): 
		self.hovered_color = colors.PURPLE if self.color != colors.PURPLE else colors.GRAY
		sounds.play_alarm()

	def on_unhover(self): self.hovered_color = colors.YELLOW

	def interact(self):
		sounds.play_blop22()
		self.hovered_color = colors.GRAY
        #print(f"Object '{self.name}' creating event with args: {self.event_args}")  # Added name

		return self.event