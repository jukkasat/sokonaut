
class GameState:
    def __init__(self):
        self.current_level = 0
        self.moves = 0
        self.original_maps = self._init_maps()
        # Make a deep copy for gameplay - need to copy each row in each map
        self.maps = [[row[:] for row in map] for map in self.original_maps]
        self.map = [row[:] for row in self.original_maps[self.current_level]]
        self.height = len(self.map)
        self.width = len(self.map[0])

    def _init_maps(self):
        return [
            # Level 1
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 2, 0, 0, 0, 0, 1, 0, 0, 1, 5, 0, 0, 0, 0, 0, 1],
            [1, 3, 0, 1, 5, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            # Level 2
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 5, 0, 0, 0, 0, 1, 3, 0, 1, 5, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 5, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            # Level 3
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        ]
    
    def new_game(self):
        # Reset the game to its initial state
        self.current_level = 0
        self.moves = 0
        self.map = [row[:] for row in self.original_maps[self.current_level]]
    
    def find_robo(self):
        # Find the robot's current position on the map
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [4, 6]:
                    return (y, x)
        
    def move(self, move_y, move_x):
        # Move the robot and handle interactions with the environment
        robo_old_y, robo_old_x = self.find_robo()
        robo_new_y = robo_old_y + move_y
        robo_new_x = robo_old_x + move_x

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

    def restart_level(self):
        self.map = [row[:] for row in self.original_maps[self.current_level]]
        self.moves = 0
    
    def level_won(self):
        # Check if all targets are covered by boxes
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [2, 6]:
                    return False
        return True
    
    def game_completed(self):
        return self.level_won() and self.current_level == len(self.maps) - 1