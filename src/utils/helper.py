import os
import sys

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