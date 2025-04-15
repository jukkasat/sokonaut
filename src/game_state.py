from maps import get_maps

class GameState:
    def __init__(self):
        self.current_level = 0
        self.moves = 0
        self.original_maps = get_maps()

        self.level_score = 100
        self.total_score = 0
        
        # Make a deep copy for gameplay - need to copy each row in each map
        self.maps = [[row[:] for row in map] for map in self.original_maps]
        self.map = [row[:] for row in self.original_maps[self.current_level]]
        
        # Update dimensions when loading new map
        self._update_dimensions()

    def _update_dimensions(self):
        # Update map dimensions after loading a new level
        self.height = len(self.map)
        self.width = len(self.map[0])

    def start_level(self, level):
        """Start a specific level"""
        if 0 <= level < len(self.original_maps):
            self.current_level = level
            self.moves = 0
            self.level_score = 100
            # Create a deep copy of the map
            self.map = [row[:] for row in self.original_maps[level]]
            # Update dimensions for the new map
            self._update_dimensions()
            # Also update the maps array with the new map
            self.maps[level] = [row[:] for row in self.original_maps[level]]
    
    def new_game(self):
        # Reset the game to its initial state
        self.current_level = 0
        self.moves = 0
        self.map = [row[:] for row in self.original_maps[self.current_level]]
    
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

        # Check if level is won - prevent movement if true
        if self.level_won():
            return
        
        # Find robot position
        robot_pos = self.find_robo()
        if not robot_pos:
            return  # Return if robot not found

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
        if self.map[robo_new_y][robo_new_x] in [3, 5]:
            laatikon_uusi_y = robo_new_y + move_y
            laatikon_uusi_x = robo_new_x + move_x

            # Check if the box can be moved
            if self.map[laatikon_uusi_y][laatikon_uusi_x] in [1, 3, 5]:
                return

            # Update the map for the box's new position
            self.map[robo_new_y][robo_new_x] -= 3
            self.map[laatikon_uusi_y][laatikon_uusi_x] += 3

        # Update the map for the robot's new position
        self.map[robo_old_y][robo_old_x] -= 4
        self.map[robo_new_y][robo_new_x] += 4

        # Increment the move counter
        self.moves += 1
        self.level_score = max(0, self.level_score - 1)

        # If level is won after this move, add level score to total
        if self.level_won():
            self.total_score += self.level_score

    def restart_level(self):
        self.map = [row[:] for row in self.original_maps[self.current_level]]
        self.moves = 0
    
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
    
    def game_completed(self):
        """Check if all levels are completed"""
        return (self.level_won() and 
                self.current_level == len(self.original_maps) - 1)