from src.maps import get_maps
from src.utils.helper import deep_copy_map

class GameState:
    def __init__(self, audio_manager):
        self.current_level = 0
        self.moves = 0
        self.original_maps = get_maps()
        self.audio_manager = audio_manager

        self.level_score = 100
        self.total_score = 0
        
        # Make a deep copy for gameplay - need to copy each row in each map
        self.maps = [deep_copy_map(map) for map in self.original_maps]
        self.map = [deep_copy_map(self.original_maps[self.current_level])]
        
        # Reset all maps to original state
        self.reset_all_maps()

        # Update dimensions when loading new map
        self._update_dimensions()

    def new_game(self):
        # Reset the game to its initial state
        self.current_level = 0
        self.moves = 0
        self.level_score = 100
        self.total_score = 0
        self.reset_all_maps()

    def start_level(self, level):
        """Start a specific level"""
        if 0 <= level < len(self.original_maps):
            self.current_level = level

            # Reset moves and scores
            self.moves = 0
            self.level_score = 100
            self.total_score = 0

            # Reset ALL maps to their original state
            self.reset_all_maps()
            # Create a deep copy of the map
            self.map = deep_copy_map(self.original_maps[level])
            # Update dimensions for the new map
            self._update_dimensions()
            # Also update the maps array with the new map
            self.maps[level] = deep_copy_map(self.original_maps[level])
            
    def find_robo(self):
        """Find the robot's current position on the map"""
        # Get current map dimensions
        height = len(self.map)
        width = len(self.map[0])
        
        # Find the robot's current position on the map
        for y in range(height):
            for x in range(width):
                if self.map[y][x] in [4, 6]:
                    return (y, x)
        return None  # Return None if robot not found
    
    def move(self, move_y, move_x):
        """Move the robot and handle interactions with the environment"""
        
        # Find robot position
        robo_old_y, robo_old_x = self.find_robo()
        robo_new_y = robo_old_y + move_y
        robo_new_x = robo_old_x + move_x

        # Check if new position is within map bounds
        if not (0 <= robo_new_y < len(self.map) and 0 <= robo_new_x < len(self.map[0])):
            return

        # Check if the new position is a wall
        if self.map[robo_new_y][robo_new_x] == 1:
            return

        # Handle box movement
        boxes_in_target_before = self.count_boxes_in_target()

        if self.map[robo_new_y][robo_new_x] in [3, 5]:
            box_new_y = robo_new_y + move_y
            box_new_x = robo_new_x + move_x

            # Check if the box can be moved
            if self.map[box_new_y][box_new_x] in [1, 3, 5]:
                return

            # Update the map for the box's new position
            self.map[robo_new_y][robo_new_x] -= 3
            self.map[box_new_y][box_new_x] += 3

        # Update the map for the robot's new position
        self.map[robo_old_y][robo_old_x] -= 4
        self.map[robo_new_y][robo_new_x] += 4

        # Update moves and decrease level score
        self.moves += 1
        self.level_score = max(0, self.level_score - 1)

        # Play barrel ready sound
        boxes_in_target_after = self.count_boxes_in_target()

        if boxes_in_target_after > boxes_in_target_before:
            self.audio_manager.play_sound("barrel_ready")

        # If level is won after this move, add level score to total
        if self.level_won():
            self.audio_manager.play_sound("level_won")
            boxes_in_target = self.count_boxes_in_target()
            target_bonus = boxes_in_target * 21
            self.level_score += target_bonus
            self.total_score += self.level_score

    def complete_level(self):
        """Advance to the next level or end the game if all levels are completed."""
        if self.level_won():
            if self.current_level < len(self.original_maps) - 1:
                self.current_level += 1
                self.map = [row[:] for row in self.original_maps[self.current_level]]
                self.moves = 0
                self.level_score = 100
                return "next_level"  # Indicate that the level was completed
            else:
                return "game_completed"  # Indicate that all levels are completed
        return None

    def level_won(self):
        """Check if all targets are covered by boxes"""
        # First ensure dimensions are up to date
        height = len(self.map)
        width = len(self.map[0])
        
        for y in range(height):
            for x in range(width):
                if self.map[y][x] in [2, 6]:
                    return False
        return True
    
    def restart_level(self):
        self.map = [row[:] for row in self.original_maps[self.current_level]]
        self.moves = 0
        self.level_score = 100
    
    def game_completed(self):
        """Check if all levels are completed"""
        return (self.level_won() and 
                self.current_level == len(self.original_maps) - 1)
    
    def count_boxes_in_target(self):
        """Count how many boxes are on target spots"""
        count = 0
        height = len(self.map)
        width = len(self.map[0])
        
        for y in range(height):
            for x in range(width):
                if self.map[y][x] == 5:  # Box on target
                    count += 1
        return count

    def _update_dimensions(self):
        # Update map dimensions after loading a new level
        self.height = len(self.map)
        self.width = len(self.map[0])

    def reset_all_maps(self):
        """Reset all maps to their original state"""
        # Make fresh deep copies of all maps
        self.maps = [deep_copy_map(map) for map in self.original_maps]
        self.map = deep_copy_map(self.original_maps[self.current_level])
        self._update_dimensions()
    