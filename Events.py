class BaseEvent:
	def __init__(self):
		pass

class ChangeRoomEvent(BaseEvent):
	def __init__(self, target_room):
		self.target_room = target_room

class AlternateRoomEvent(BaseEvent):
	def __init__(self, first_room, second_room):
		self.first_room = first_room
		self.second_room = second_room

class AddItemEvent(BaseEvent):
	def __init__(self, item):
		self.item = item