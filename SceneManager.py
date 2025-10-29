# Scenes include Rooms, but also Main Menus and Game Event Screens (Game Over, Game End)

from Scenes.Room import Room
from Scenes.BaseScene import BaseScene
class SceneMgr:
	def __init__(self, surface, Rooms={}, Scenes={}):
		self.Rooms = Rooms
		self.Scenes = Scenes

		self.current_scene = None

		self.surface = surface

		self.main_menu = None

	def ready(self):
		self.current_scene = self.Rooms["START"] if not self.main_menu else self.main_menu
		self.current_scene.load_scene(self.surface)

	# TODO: Maybe there's a better implementation to get mouse_pos
	def update(self, mouse_pos):

		for obj in self.current_scene.get_objects():
			obj.check_hover(mouse_pos)
			
		self.current_scene.update_scene()

	def add_room(self, room): self.add_scene(room)
	def add_scene(self, scene):
		# Adds an item object with the key being the item's ID
		self.Scenes[scene.ID] = scene

		# // Maybe there's no need for this
		if isinstance(scene, Room): self.Rooms[scene.ID] = scene

	# Adds multiple scenes by calling add_scene for each one 
	# // Meybe there's a better implementation
	def add_scenes(self, scenes):
		for scene in scenes:
			self.add_scene(scene)

	def set_current_scene(self, scene): 
		if not isinstance(scene, BaseScene):
			return

		self.current_scene = scene
		self.current_scene.load_scene(self.surface)

#	Returns first hovered object or None if so (if none)
	def get_hovered_object(self):
		for obj in self.current_scene.get_objects():
			if obj.is_hovered:
				return obj 
		return None

	def get_room(self, room_ID): return self.Rooms[room_ID]
	def get_scene(self, scene_ID): return self.Scenes[scene_ID]

	def get_current_scene(self): return self.current_scene

	def get_rooms(self): return self.Rooms
	def get_scenes(self): return self.Scenes