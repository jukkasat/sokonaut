import json
import os

def get_maps():
    maps = []
    map_dir = "."
    maps_file = "maps.json"

    try:
        with open(os.path.join(map_dir, maps_file), 'r') as f:
            level_data = json.load(f)
            maps = level_data["maps"]
    except Exception as e:
        print(f"Error loading level file {maps_file}: {e}")
        # If a level fails to load, insert a default empty level
        maps = [[[]]]
    return maps