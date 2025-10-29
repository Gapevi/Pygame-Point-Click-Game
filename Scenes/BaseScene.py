from abc import ABC, abstractmethod
class BaseScene(ABC):
	def __init__(self, ID, name, background_image_path, 
					objects_list=[], *, bg_img_position=(0, 0)):

		self.ID = ID
		self.name = name
		self.objects = objects_list

		self.bg_img_path = background_image_path
		self.bg_img_position = bg_img_position

	def load_scene(self, surface): pass 
	def update_scene(self): pass

	def on_load_scene(self): pass

	def add_object(self, obj): self.objects.append(obj)
	def add_objects(self, objs): self.objects.extend(objs)
	
	def get_objects(self): return self.objects