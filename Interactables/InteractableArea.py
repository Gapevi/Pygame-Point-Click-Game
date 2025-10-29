import pygame
from abc import ABC, abstractmethod

"""
Definition of InteractableArea class

Description:
	Class that holds basic interactability properties, as seen below.

Constructor:
	name: 			str 	= Name of the Sprite 
	description:	str 	= Description of the Sprite
	event:		BaseEvent	= Game event returned when object is interacted
	enabled:		bool	= Used as reference to cease interaction
	color:			(r,g,b)	= The color of the object when inactive
	hovered_color: 	(r,g,b)	= The color of the object when is_hovered is true
	transparency:	int 	= How transparent is the object (0-> transparent - 255 -> normal)
"""

class BaseInteractableArea(ABC):
	def __init__(self, area, name, description, *, event=None, 
				enabled = True, color = None, hovered_color = None,
				transparency = 255):
		self.name:str=name
		self.description:str=description

		self.event = event

		if isinstance(area, pygame.Rect): self.area = area
		else: self.area = pygame.Rect(area)

		self.is_hovered = False
		self.clicked_count = 0

		self.transparency = transparency

		self.color = color
		self.hovered_color = hovered_color

		self.enabled = enabled

		self.clicked_count = 0

	def handle_click(self):
		if not self.enabled: return
		self.on_clicked()
		return f"{self.description} (clicked {self.clicked_count} times)"

	def check_hover(self, pos):
		if not self.enabled: return
		if self.area.collidepoint(pos):
			self._hover()
		else:
			self._unhover()
		return self.is_hovered

	@abstractmethod
	def on_clicked(self): pass
	@abstractmethod
	def interact(self): pass

	def on_hover(self): pass
	def on_unhover(self): pass

	def _hover(self):
		self.is_hovered = True
		self.on_hover()
	def _unhover(self):
		self.is_hovered = False
		self.on_unhover()

	def ready(self, screen=None): pass
	def draw(self, screen=None): pass