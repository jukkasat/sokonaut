import pygame
from src.state.state import State

class LevelWonState(State):
    def __init__(self, sokonaut):
        super().__init__(sokonaut)

    def handle_input(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return self._return_to_menu()
            
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_F2, pygame.K_ESCAPE):
                    return self._return_to_menu()
                
                elif event.key == pygame.K_RETURN:
                    return self._handle_next_level()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check if next level text was clicked
                if (self.sokonaut.renderer.level_won_view.next_level_rect and 
                    self.sokonaut.renderer.level_won_view.next_level_rect.collidepoint(x, y)):
                    return self._handle_next_level()

                if self.sokonaut.renderer.ui_drawer.quit_rect and \
                self.sokonaut.renderer.ui_drawer.quit_rect.collidepoint((x, y)):
                    self._return_to_menu()

        return None

    def _handle_next_level(self):
        """Helper method to handle next level logic"""
        result = self.sokonaut.game_state.complete_level()
        if result == "next_level":
            self.sokonaut.scores.mark_level_completed(self.sokonaut.game_state.current_level - 1)
            self.sokonaut.audio_manager.play_music("level")
            return "next_level"
        elif result == "game_completed":
            return "game_completed"
        return None

    def draw(self):
        self.sokonaut.renderer.draw()
