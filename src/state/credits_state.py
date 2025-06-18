import sys
import pygame
from src.state.menu_state import MenuState

class CreditsState(MenuState):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)
        self.menu = sokonaut.menu.credits_menu

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                    self.sokonaut.audio_manager.play_sound("select")
                    self.sokonaut.current_state = self.sokonaut.main_menu_state
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if self.menu.back_rect.collidepoint(pygame.mouse.get_pos()):
                        self.sokonaut.audio_manager.play_sound("select")
                        self.sokonaut.current_state = self.sokonaut.main_menu_state

        return None

    def draw(self):
        self.sokonaut.menu.credits_menu.draw()