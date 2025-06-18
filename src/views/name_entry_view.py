from src.views.menu_base import MenuBase
from src.utils.helper import center_text, center_rect

class NameEntryView(MenuBase):
    def __init__(self, display, renderer, scores):
        super().__init__(display, renderer, scores)
        self.current_name = ""
        self.score = 0

    def draw(self):
        # Create background for name entry view
        menu_width = 400
        menu_height = 200
        menu_x, menu_y = center_rect(self.display, menu_width, self.display.get_height() // 2 - menu_height // 2)
        self.draw_menu_background(menu_width, menu_height, menu_x, menu_y)

        # Draw text
        text = self.menu_font_small.render("New High Score!", True, (210, 105, 30))
        score_text = self.menu_font_small.render(f"Score: {self.score}", True, (200, 200, 200))
        name_text = self.menu_font_small.render("Enter your name:", True, (200, 200, 200))
        input_text = self.menu_font_small.render(self.current_name + "_", True, (200, 200, 200))
        
        text_rect = center_text(self.display, text, menu_y + 30)
        self.display.blit(text, text_rect)
        score_rect = center_text(self.display, score_text, menu_y + 60)
        self.display.blit(score_text, score_rect)
        name_rect = center_text(self.display, name_text, menu_y + 90)
        self.display.blit(name_text, name_rect)
        input_rect = center_text(self.display, input_text, menu_y + 120)
        self.display.blit(input_text, input_rect)
