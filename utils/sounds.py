import pygame
from .resource_path import resource_path
pygame.mixer.init()

alarm = pygame.mixer.Sound(resource_path("assets/sounds/Alarm.wav"))
blop22 = pygame.mixer.Sound(resource_path("assets/sounds/Blop22.wav"))
swoosh07 = pygame.mixer.Sound(resource_path("assets/sounds/RetroSwooosh07.wav"))
swoosh16 = pygame.mixer.Sound(resource_path("assets/sounds/RetroSwooosh16.wav"))
punch07 = pygame.mixer.Sound(resource_path("assets/sounds/RetroImpactPunch07.wav"))

VOLUME_SND :float= .75

sounds = [alarm, blop22, swoosh07, swoosh16, punch07]

SOUNDS = {
	"alarm": alarm,
	"blop22": blop22,
	"swoosh07": swoosh07,
	"swoosh16": swoosh16,
	"punch07": punch07,
}

for sound in sounds:
	sound.set_volume(VOLUME_SND)

def play_sound(soundID):
	pygame.mixer.Sound.play(SOUNDS.get(soundID))

def play_blop22():
	pygame.mixer.Sound.play(blop22)

def play_alarm():
	pygame.mixer.Sound.play(alarm)

def play_swoosh():
	pygame.mixer.Sound.play(swoosh16)

def play_punch():
	pygame.mixer.Sound.play(punch07)