class BaseInventory:
	def __init__(self, items=[]):
		self.items = items

		self.max_size = 16 # (0 to 15)
		self.current_size = self._get_number_of_items() # Current number of items


	def get_items(self):
		return self.items

#	Returns a list of all items with the class '_class'
	def get_items_class(self, _class):
		return [item for item in self.items if isinstance(item, _class)]

#	Adding and removing
	def add_item(self, item): 
		if self._check_full([item]):
			return

		self.items.append(item) # Appends a single item
		self._update_current_size()
		print(f"Added item {item.name} to inventory")
		
	def add_items(self, items): 
		if self._check_full(items):
			return

		self.items.extend(items) # Appends multiple items
		self._update_current_size()

	def remove_item(self, item):
		if not item in self.items:
			print("Item not in list")
			return

		self.items.pop( self.items.index(item) )
		self._update_current_size()

	def remove_index(self, index):
		self.items.pop(index)
		self._update_current_size()

	def _check_full(self, items): 
		if (len(items) + 1) + self.current_size > self.max_size:
			return True
		return False 
		
	def _get_number_of_items(self): return len(self.items) + 1
	def _update_current_size(self): self.current_size = self._get_number_of_items()
	def _clear(self): self.items.clear()

class PlayerInventory(BaseInventory):
	def __init__(self, items=[]):
		super().__init__(items)

		self.size = 8

