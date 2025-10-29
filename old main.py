# Import necessary libraries
import pygame
from pygame.locals import *

from Interactables.BaseInteractableRect import TestBaseInteractableRect
from Scenes.Room import Room
from Interactables.BaseInteractableSprite import TestInteractableSprite

import Events
import utils.colors as colors
from utils.fonts import font, small_font

from camera import Camera

from Player import Player

from Item import TestItem, TestItemSprite

from SceneManager import SceneMgr

pygame.init()

# TODO:
# Make sprites hide when changing rooms
# Make so position works like position.x = game_surface.width * pos_x (pos_x is 0-100)
# There's ton of useless code in this

# Set up the game window
screen_width, screen_height = 1280, 720 #800*1.8, 600*1.3
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point 'n' Click Game")

# Surface that is used for the game
game_surface = pygame.Surface((screen_width*2, screen_height*2))

running = True
clock = pygame.time.Clock()

delta_time = 0.1

all_sprites = pygame.sprite.Group()

scn_mgr = SceneMgr()

##+ PLAYER
    
player = Player()

##- PLAYER

message_timer = 0
message = "click"

item1 = TestItemSprite("Key", 
                    "This is an item", 
                    "assets/images/gapovi.jpg",
                    all_sprites,
                    )
item1.event = Events.AddItemEvent(item1)

objects = [TestBaseInteractableRect((100, 250, 120, 150),
                            "Nothing",
                             "This is a tst object",
                             color=colors.BROWN,
                             hovered_color=colors.YELLOW,
                             transparency=64,),
                            
            TestBaseInteractableRect(((300, 150, 100, 80)),
                                 "Goto Room2",
                                 "Right Click to go to room2",
                                 event=Events.ChangeRoomEvent("room2"),
                                 color=colors.BROWN,
                                 hovered_color=colors.YELLOW,
                                 )
    ]
objects.append(item1)
##+ region SPRITE

door = TestInteractableSprite("Gapovi",
                                "assets/images/temp_door.jpg",
                                "a door",
                                all_sprites,
                                (750, 200),
                                event=Events.AlternateRoomEvent("living_room", "room1"),
                                )

sprites = [door]

objects.extend(sprites)

##- region SPRITE

##+ ROOM

room1 = Room("Room 1",
                "room1",
                "assets/images/cave.jpg",
                game_surface,
                objects)

room2 = Room("Room 2",
                "room2",
                "assets/images/hole.jpg",
                game_surface,
                [TestBaseInteractableRect(((450, 150, 100, 100)),
                    "Go back",
                    "Right Click to go to Room1",
                    event=Events.ChangeRoomEvent("room1"),
                    color=colors.BROWN,
                    hovered_color=colors.YELLOW,
                )]
            )

living_room = Room("Living Room",
                    "living_room",
                    "assets/images/living_room.jpg",
                    game_surface,
                    [door])

scn_mgr.add_scenes([room1, room2, living_room])

current_room = scn_mgr.get_room("room1")

##- region ROOM


camera = Camera(screen.get_width(), screen.get_height())
camera.smooth_factor = 0.1
def update():
    global running, delta_time, message_timer, message

   # mouse_pos = pygame.mouse.get_pos()

    mouse_pos = camera.update(pygame.mouse.get_pos())

    current_room.update_scene()

    #all_sprites.draw(game_surface)

#   Scn Mgr thing
    for obj in current_room.get_objects():
        obj.check_hover(mouse_pos)
    for sprite in sprites:
        sprite.check_hover(mouse_pos)

    # Blit puts a Surface ontop of another surface
    #game_surface.blit(cave_img, (30, 30))

#   ScnMgr/Scn thing?
    # Draw cursor hint
    hovered_obj = None
    for obj in current_room.get_objects():
        if obj.is_hovered:
            hovered_obj = obj
            break
    for sprite in sprites:
        if sprite.is_hovered:
            hovered_obj = sprite 

#   ScnMgr/Scn thing?
    if hovered_obj:
        cursor_text = small_font.render(f"{hovered_obj.description}", True, colors.WHITE)
        game_surface.blit(cursor_text, (mouse_pos[0] + 15, mouse_pos[1] + 15))

    screen.fill((0, 0, 0))  # Clear screen first
    screen.blit(game_surface, (-camera.offset_x, -camera.offset_y))

    #   Updates game_surface
    pygame.display.flip()
    #   Limits to 60 fps
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, 0.1)

MOUSE_LEFT_BUTTON =   1
MOUSE_MIDDLE_BUTTON = 2
MOUSE_RIGHT_BUTTON =  3
MOUSE_SCROLL_UP =     4
MOUSE_SCROLL_DOWN =   5

def _event():
    global running, current_room, events

    events = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 

#       Most is player stuff
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT_BUTTON: 
                clicked_smthg = False
                for obj in current_room.get_objects():
                    if obj.is_hovered:
                        response = obj.handle_click()
                        clicked_smthg = True
                        break
            if event.button == MOUSE_RIGHT_BUTTON:
                clicked_smthg = False
                for obj in current_room.get_objects():
                    if obj.is_hovered:
                        obj_event = obj.interact()
                        if obj_event and isinstance(obj_event, Events.BaseEvent):
                            events.append(obj_event)

                if not clicked_smthg:
                    message = "Nothing to interact"
                    message_timer = 120

    handle_events(events)
    events.clear()

def handle_events(events):
    global current_room

    if events == []:
        return

    for event in events:
        if isinstance(event, Events.ChangeRoomEvent):
            current_room = scn_mgr.get_room(event.target_room)

        elif isinstance(event, Events.AlternateRoomEvent):
            current_room = scn_mgr.get_room(event.first_room) if current_room.ID != event.first_room else scn_mgr.get_room(event.second_room)

        elif isinstance(event, Events.AddItemEvent):
            player.Inventory.add_item(event.item)

while running:
    _event()
    update()

pygame.quit()