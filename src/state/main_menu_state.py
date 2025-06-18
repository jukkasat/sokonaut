import sys
import pygame
from src.state.menu_state import MenuState

class MainMenuState(MenuState):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.menu = sokonaut.menu.main_menu
        self.audio_manager = sokonaut.audio_manager
        self.menu.draw() # Draw the menu once to initialize menu_item_rects

    def handle_input(self):
        for event in pygame.event.get():
            action = None
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP:
                    self.menu.selected_item = (self.menu.selected_item - 1) % len(self.menu.menu_items)
                    self.audio_manager.play_sound("menu_select")
                elif event.key == pygame.K_DOWN:
                    self.menu.selected_item = (self.menu.selected_item + 1) % len(self.menu.menu_items)
                    self.audio_manager.play_sound("menu_select")
                elif event.key == pygame.K_RETURN:
                    action = self._handle_selection()

            # Handle mouse input
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(self.menu.menu_item_rects):
                    if rect.collidepoint(mouse_pos):
                        if self.menu.selected_item != i:
                            self.menu.selected_item = i
                            self.audio_manager.play_sound("menu_select")
                        break
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Mouse left click
                    mouse_pos = pygame.mouse.get_pos()

                    # Check menu item clicks
                    for i, rect in enumerate(self.menu.menu_item_rects):
                        if rect.collidepoint(mouse_pos):
                            self.selected_item = i
                            action = self._handle_selection()
                        
                    # Check music icon click
                    if hasattr(self, 'music_icon_rect') and self.music_icon_rect.collidepoint(mouse_pos):
                        self.menu.music_enabled = not self.menu.music_enabled
                        self.audio_manager.toggle_audio(self.menu.music_enabled)
                        if self.menu.music_enabled:
                            self.audio_manager.play_sound("select")
                

            # action = self.sokonaut.menu.main_menu.handle_input(event)
            if action == "new_game":
                self.audio_manager.play_sound("select")
                return "new_game"
            elif action == "levels":
                self.audio_manager.play_sound("select")
                self.sokonaut.current_state = self.sokonaut.levels_menu_state
            elif action == "high_score":
                self.audio_manager.play_sound("select")
                self.sokonaut.current_state = self.sokonaut.high_score_state
            elif action == "credits":
                self.audio_manager.play_sound("select")
                self.sokonaut.current_state = self.sokonaut.credits_state
            elif action is not None:
                self.audio_manager.play_sound("select")
                return action
        return None

    def _handle_selection(self):
        # Handle selection in the main menu
        selected = self.menu.menu_items[self.menu.selected_item]
        if selected == "new game":
            return "new_game"
        elif selected == "levels":
            return "levels"
        elif selected == "high score":
            return "high_score"
        elif selected == "credits":
            return "credits"
        elif selected == "quit":
            pygame.quit()
            sys.exit()
        return None

    def draw(self):
        self.sokonaut.menu.main_menu.draw()