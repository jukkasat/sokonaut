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