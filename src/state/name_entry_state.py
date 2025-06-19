import pygame
from src.state.menu_state import MenuState

class NameEntryState(MenuState):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.menu = sokonaut.menu.name_entry_view
        self.confirm_rect = None
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._return_to_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.menu.current_name = self.menu.current_name[:-1]
                elif event.key == pygame.K_RETURN:

                    if len(self.menu.current_name) >= 1:
                        self.sokonaut.scores.add_score(self.menu.current_name, self.sokonaut.game_state.total_score)
                        self.sokonaut.menu.current_name = self.menu.current_name
                        
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
                    
                elif len(self.menu.current_name) < 15:
                    if event.unicode.isalnum():
                        self.menu.current_name += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.menu.confirm_rect and self.menu.confirm_rect.collidepoint(event.pos):
                        if len(self.menu.current_name) >= 2:
                            self.sokonaut.scores.add_score(self.menu.current_name, self.sokonaut.game_state.total_score)
                            self.sokonaut.menu.current_name = self.menu.current_name
                            if self.sokonaut.game_state.game_completed():
                                self.sokonaut.current_state = self.sokonaut.game_won_state
                            else:
                                self.sokonaut.current_state = self.sokonaut.main_menu_state
                                self.sokonaut.audio_manager.play_music("menu")
                            return "game_won" if self.sokonaut.game_state.game_completed() else "main_menu"
        return None

    def draw(self):
        self.menu.draw()