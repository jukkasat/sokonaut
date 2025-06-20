import os
import sys
import pygame

def center_text(surface, text, y):
    """Centers text horizontally on the surface at the given y-coordinate."""
    text_rect = text.get_rect(center=(surface.get_width() // 2, y))
    return text_rect

def center_rect(surface, width, y):
     """Centers rectangle horizontally on the surface at the given y-coordinate."""
     x = surface.get_width() // 2 - width // 2
     return (x, y)

def deep_copy_map(map_data):
    """Creates and returns a deep copy of the given map data."""
    return [row[:] for row in map_data]

def get_base_path(name):
    """Determine and return the correct directory or file path.
    - PyInstaller: files are directly in the root directory (sys._MEIPASS)
    - Development environment: root files (maps.json, etc.) can be found at the root of the project and folders (img, audio) under src
    """
    if hasattr(sys, '_MEIPASS'): # PyInstaller
        return os.path.join(sys._MEIPASS, name)
    else: # Dev: 
        root = os.path.dirname(os.path.dirname(__file__))
        if name.endswith('.json'):
            return os.path.join(root, '..', name)
        else:
            return os.path.join(root, name)
        
def get_audio_icons():
    try:
        audio_on_icon = pygame.image.load(get_base_path("img") + "/audio_on.png")
        audio_off_icon = pygame.image.load(get_base_path("img") + "/audio_off.png")
        icon_size = (74, 74)
        audio_on_icon = pygame.transform.scale(audio_on_icon, icon_size)
        audio_off_icon = pygame.transform.scale(audio_off_icon, icon_size)
    except:
        print("Could not load music control icons")
        audio_on_icon = None
        audio_off_icon = None

    return audio_on_icon, audio_off_icon