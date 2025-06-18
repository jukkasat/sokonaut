import pygame
from src.state.menu_state import MenuState

class LevelsMenuState(MenuState):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.menu = sokonaut.menu.levels_menu

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Move selection up
                    if self.menu.selected_level == 0:
                        self.menu.selected_level = -1  # Select back button
                    elif self.menu.selected_level == -1:  # If on back button
                        self.menu.selected_level = self.menu.total_levels - 1  # Go to last level
                    else:
                        self.menu.selected_level = (self.menu.selected_level - 1)
                    self.audio_manager.play_sound("select")
                
                elif event.key == pygame.K_DOWN:
                    # Move selection down
                    if self.menu.selected_level == -1:  # If on back button
                        self.menu.selected_level = 0  # Go to first level
                    elif self.menu.selected_level == self.menu.total_levels - 1:
                        self.menu.selected_level = -1  # Go to back button
                    else:
                        self.menu.selected_level = (self.menu.selected_level + 1)
                    self.audio_manager.play_sound("select")
                
                if event.key == pygame.K_RETURN:
                    if self.menu.selected_level == -1:  # Back button selected
                        self._return_to_menu()
                    elif (self.sokonaut.scores.is_level_unlocked(self.menu.selected_level)):
                        self.audio_manager.play_sound("select")
                        self.sokonaut.game_state.start_level(self.menu.selected_level)
                        self.sokonaut.current_state = self.sokonaut.game_playing_state
                        return f"start_level_{self.menu.selected_level}"
                if event.key == pygame.K_ESCAPE:
                    self._return_to_menu()
            
            # Handle mouse input
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()

                # Check level buttons
                old_selected = self.menu.selected_level
                for rect, level in self.menu.level_rects:
                    if rect.collidepoint(mouse_pos):
                        self.menu.selected_level = level
                        if old_selected != level:
                            self.audio_manager.play_sound("level_select")
                        break
                if self.menu.back_rect.collidepoint(mouse_pos):
                    if self.menu.selected_level != -1:
                        self.menu.selected_level = -1
                        self.audio_manager.play_sound("level_select")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    # Check level buttons
                    for rect, level in self.menu.level_rects:
                        if rect.collidepoint(mouse_pos):
                            if self.sokonaut.scores.is_level_unlocked(level):
                                return f"start_level_{level}"
                            break
                    # Check back button
                    if self.menu.back_rect.collidepoint(mouse_pos):
                        self._return_to_menu()

        return None

    def draw(self):
        self.sokonaut.menu.levels_menu.draw()