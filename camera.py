class Camera:
    def __init__(self, screen_width, screen_height):
        self.offset_x = 0
        self.offset_y = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.smooth_factor = 0.1
        self.max_offset = 80

#       // Moved from update() cuz the dimensions of screen are static
        self.screen_center_x = self.screen_width / 2
        self.screen_center_y = self.screen_height / 2

#   Updates camera and returns new mouse position 
    def update(self, mouse_pos):
        
        mouse_offset_x = mouse_pos[0] - self.screen_center_x
        mouse_offset_y = mouse_pos[1] - self.screen_center_y
        
        target_x = (mouse_offset_x / self.screen_width) * self.max_offset * 2
        target_y = (mouse_offset_y / self.screen_height) * self.max_offset * 2
        
        target_x = max(-self.max_offset, min(self.max_offset, target_x))
        target_y = max(-self.max_offset, min(self.max_offset, target_y))
        
        self.offset_x += (target_x - self.offset_x) * self.smooth_factor
        self.offset_y += (target_y - self.offset_y) * self.smooth_factor

        adjusted_mouse_x = mouse_pos[0] + self.offset_x
        adjusted_mouse_y = mouse_pos[1] + self.offset_y

        adjusted_mouse_pos = (adjusted_mouse_x, adjusted_mouse_y)

        return adjusted_mouse_pos