from abc import ABC, abstractmethod
from Interactables.BaseInteractableSprite import BaseInteractableSprite
class BaseItem(ABC):
	def __init__(self, name, description, *, event=None, stackable=False):
		self.name = name
		self.description = description

		self.stackable = stackable

		self.event = event

	def use(self): pass

class BaseItemSprite(BaseInteractableSprite, BaseItem, ABC):
	def __init__(self, name, description, image_path, group, *, position=(0,0), event=None):
		BaseItem.__init__(self, name, description)
		BaseInteractableSprite.__init__(self, name, image_path, description, group, position, event=event)

	@abstractmethod
	def interact(self): return self.event
	@abstractmethod
	def on_clicked(self): pass

class TestItem(BaseItem):
	def __init__(self, name, description, **kwargs):
		super().__init__(name, description, **kwargs)

class TestItemSprite(BaseItemSprite):
	def __init__(self, name, description, image_path, group, *, position=(0,0), event=None):
		super().__init__(name, description, image_path, group, position=position, event=event)

	def interact(self): return self.event

	def on_clicked(self): pass
