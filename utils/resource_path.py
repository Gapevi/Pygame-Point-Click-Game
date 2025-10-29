import os
import pygame
import sys

# Use this to ensure relative path works for both dev and compiled versions
def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

    #base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    #return os.path.join(base_path, relative_path)