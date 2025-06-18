import pygame
from src.state.menu_state import MenuState

class NameEntryState(MenuState):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.menu = sokonaut.menu.name_entry_menu
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._return_to_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.sokonaut.menu.name_entry_menu.current_name = self.sokonaut.menu.name_entry_menu.current_name[:-1]
                elif event.key == pygame.K_RETURN:
                    self.sokonaut.scores.add_score(self.sokonaut.menu.name_entry_menu.current_name, self.sokonaut.game_state.total_score)
                    self.sokonaut.menu.current_name = self.sokonaut.menu.name_entry_menu.current_name
                    
                    # If game completed, return to game_won state
                    if self.sokonaut.game_state.game_completed():
                        self.sokonaut.current_state = self.sokonaut.game_won_state
                    else:
                        self.sokonaut.current_state = self.sokonaut.main_menu_state
                        self.sokonaut.audio_manager.play_music("menu")
                    return "game_won" if self.sokonaut.game_state.game_completed() else "main_menu"
                    
                elif event.key == pygame.K_ESCAPE:
                    if self.sokonaut.game_state.game_completed():
                        self.sokonaut.current_state = self.sokonaut.game_won_state
                    else:
                        self.sokonaut.current_state = self.sokonaut.main_menu_state
                        self.sokonaut.audio_manager.play_music("menu")
                    return "game_won" if self.sokonaut.game_state.game_completed() else "main_menu"
                    
                elif len(self.sokonaut.menu.name_entry_menu.current_name) < 15:
                    if event.unicode.isalnum():
                        self.sokonaut.menu.name_entry_menu.current_name += event.unicode
        return None

    def draw(self):
        self.sokonaut.menu.name_entry_menu.draw()