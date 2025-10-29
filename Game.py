import pygame
import Events

from Scenes.Room import Room

from episodes.episode1 import e1_scenes

class Game:

	def __init__(self, *, screen, debug=False):
		self.delta_time = 0.1

		self.screen_width = screen.get_width()
		self.screen_height = screen.get_height()

		self.running :bool= False

		self.screen = screen
		self._debug = debug

	def run(self) -> bool:
		_event_successfull :bool= self._event()
		_update_successfull :bool= self.update()

		# Returns False if either of them quit
		return _event_successfull and _update_successfull 

	def ready(self) -> None:
		"""
		Sets initial non constructor variables
		"""
		from Player import Player
		from camera import Camera
		from SceneManager import SceneMgr
		
		self.running = True

		self.text_surface = pygame.Surface((self.screen_width, self.screen_height))

		# Surface that is used for the game
		self.game_surface = pygame.Surface((self.screen_width, self.screen_height))

		self.player = Player()

		self.camera = Camera(self.screen_width, self.screen_height)
		self.player.set_camera(self.camera)

		self.scn_mgr = SceneMgr(self.game_surface) 

		self.current_scene = self.scn_mgr.get_current_scene()

		self.object_events = []


		self.scn_mgr.add_scenes(e1_scenes)


		self.player.ready()
		self.scn_mgr.ready()

	def update(self) -> bool:

		self.player.update()


		#print(self.scn_mgr.get_current_scene().get_objects())
		self.scn_mgr.update(self.player.get_mouse_pos())

		self.screen.fill((0, 0, 0))  # Clear screen first

		self.screen.blit(self.game_surface, (-self.camera.offset_x, -self.camera.offset_y))

		self.player.update_text(self.text_surface, self.scn_mgr.get_hovered_object())

		self.game_surface.fill((0, 0, 0))

		return self.running

	def _event(self) -> bool:
		"""
		Handles python standard events
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False

			elif event.type == pygame.KEYDOWN:
				self.handle_key_input(event.key)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.handle_mouse_input(event.button)

		self.handle_events()
		self.object_events.clear()

		return self.running

	def handle_key_input(self, key) -> None:
		if key == pygame.K_ESCAPE:
			self.running = False

	def handle_mouse_input(self, button) -> None:
		MOUSE_LEFT_BUTTON =   1
		MOUSE_MIDDLE_BUTTON = 2
		MOUSE_RIGHT_BUTTON =  3
		MOUSE_SCROLL_UP =     4
		MOUSE_SCROLL_DOWN =   5

		obj_event = None

		if button == MOUSE_LEFT_BUTTON:
			for obj in self.scn_mgr.get_current_scene().get_objects():
				if obj.is_hovered:
					obj_event = obj.handle_click()
					

		elif button == MOUSE_RIGHT_BUTTON:
			for obj in self.scn_mgr.get_current_scene().get_objects():
				if obj.is_hovered:
					obj_event = obj.interact()

		# Appends event to list if exists
		if obj_event and isinstance(obj_event, Events.BaseEvent):
			self.object_events.append(obj_event)

	def handle_events(self) -> None:
		"""
		Handles events from Events module
		"""
		if self.object_events == []:
			return

		for obj_event in self.object_events:
			if isinstance(obj_event, Events.ChangeRoomEvent):
				current_room = self.scn_mgr.get_room(obj_event.target_room)

				self.scn_mgr.set_current_scene(current_room)

			elif isinstance(obj_event, Events.AlternateRoomEvent):
				current_room = self.scn_mgr.get_room(obj_event.first_room) if current_room.ID != obj_event.first_room else scn_mgr.get_room(obj_event.second_room)

				self.scn_mgr.set_current_scene(current_room)

			elif isinstance(obj_event, Events.AddItemEvent):
				self.player.Inventory.add_item(obj_event.item)
