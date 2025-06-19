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

def get_base_path(subdir):
    """Helper method to determine the correct directory or file path.
    If subdir_or_file is a directory, returns the path to that directory.
    If subdir_or_file is a json file (e.g. settings.json), returns the path to that file in the root.
    """
    if hasattr(sys, '_MEIPASS'):  # Running as PyInstaller bundle
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.dirname(__file__)) # src/utils/helper.py -> src/utils -> src

    if subdir.endswith(".json"):
        return os.path.join(os.path.dirname(base), subdir)  # workspace root
    return os.path.join(base, subdir)  # src/img tai src/audio