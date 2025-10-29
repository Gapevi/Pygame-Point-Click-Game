from Interactables.BaseInteractableRect import InteractableRect
import Events
import utils.colors as colors
from Scenes.BaseScene import BaseScene

class MainMenuScene(BaseScene):
	def __init__(self, ID, name, background_image_path=None, objects_list=[], **kwargs):
		super().__init__(ID, name, background_image_path, objects_list, **kwargs)

	def update_scene(self):
		self.surface.fill(colors.LIGHT_GRAY)
		for obj in self.objects:
			obj.draw(self.surface)

MainMenuObjects = [
			InteractableRect(
				(250, 250, 160, 160),
				"ENTER GAME",
				"Click to begin game",
				event=Events.ChangeRoomEvent("START")
				)
		]

_main_menu_scene = MainMenuScene("MAIN_MENU", "Main Menu Scene", None, MainMenuObjects)