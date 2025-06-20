import json
import os
from src.utils.helper import get_base_path

def get_maps():
    maps = []

    """Load maps from maps.json file"""
    try:
        maps_path = get_base_path("maps.json")
        
        if not os.path.exists(maps_path):
            raise FileNotFoundError(f"maps.json not found at {maps_path}")

        with open(maps_path, 'r') as f:
            maps_data = json.load(f)
            maps = maps_data["maps"]
                
            # Validate map data
            for map in maps:
                if not map or not isinstance(maps_data["maps"], list):
                    raise ValueError("Invalid map format")
                if not all(isinstance(row, list) for row in map):
                    raise ValueError("Invalid map row format")
        return maps
            
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in maps.json: {e}")
    except Exception as e:
        raise Exception(f"Error loading maps: {e}")