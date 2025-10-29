import Interactables.BaseInteractableRect
import Events
import utils.colors as colors
from Scenes.BaseScene import BaseScene

class MainMenuScene(BaseScene):
	def __init__(self, ID, name, background_image_path=None, objects_list=[], **kwargs):
		super().__init__(ID, name, background_image_path, objects_list, **kwargs)

	def update_scene(self, screen):
		screen.fill(colors.LIGHT_GRAY)

MainMenuObjects = [
			InteractableRect(
				(250, 250, 80, 160),
				"ENTER GAME",
				"Click to begin game",
				event=Events.ChangeRoomEvent("START")
				)
		]

main_menu = MainMenuScene("MAIN_MENU", "Main Menu Scene", None, MainMenuObjects)