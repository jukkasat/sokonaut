import pygame

class MobileControls:
    def __init__(self, display):
        self.display = display
        self.button_size = 85
        self.padding = 20
        self.setup_buttons()
        
    def setup_buttons(self):
        # Place buttons at bottom left of screen
        bottom_y = self.display.get_height() - self.button_size - self.padding
        left_x = self.padding * 1

        # Define button positions
        # Center button (down)
        self.down_rect = pygame.Rect(
            left_x + self.button_size + 15,
            bottom_y - self.padding,
            self.button_size, self.button_size
        )
        
        # Left button
        self.left_rect = pygame.Rect(
            left_x,  # Leftmost position
            bottom_y - self.padding * 3,
            self.button_size, self.button_size
        )
        
        # Right button
        self.right_rect = pygame.Rect(
            (left_x + self.button_size * 2) + self.padding * 1.5,
            bottom_y - self.padding * 3,
            self.button_size, self.button_size
        )
        
        # Up button (above down button)
        self.up_rect = pygame.Rect(
            left_x + self.button_size + 15,
            bottom_y - self.button_size - self.padding * 2, 
            self.button_size, self.button_size
        )

        # Calculate total size needed for controls surface
        surface_width = (self.button_size * 3) + (self.padding * 3)
        surface_height = (self.button_size * 3) + (self.padding * 3)

        # Create surface for buttons
        self.controls_surface = pygame.Surface(
            (surface_width, surface_height),
            pygame.SRCALPHA
        )

    def draw(self):
        # Clear the controls surface
        self.controls_surface.fill((0,0,0,0))
        
        # Draw all buttons using the helper method
        buttons = [
            (self.up_rect, "↑"),
            (self.down_rect, "↓"),
            (self.left_rect, "←"),
            (self.right_rect, "→")
        ]
        
        for rect, text in buttons:
            self._draw_button(rect, text)

        # Draw the entire surface to screen
        self.display.blit(
            self.controls_surface,
            (self.padding, 
             self.display.get_height() - self.controls_surface.get_height())
        )

    def _draw_button(self, rect, text, offset=False):
        """draw a single button with text"""
        # Create adjusted rect for surface drawing
        surface_rect = rect.copy()
        surface_rect.x -= self.padding
        surface_rect.y -= (self.display.get_height() - self.controls_surface.get_height())
        
        # Draw button background and border
        pygame.draw.rect(self.controls_surface, (50, 50, 50, 128), surface_rect, border_radius=24)
        pygame.draw.rect(self.controls_surface, (200, 105, 30), surface_rect, 1, border_radius=24)
        
        # Draw text
        font = pygame.font.SysFont("Arial", 36)
        text_surface = font.render(text, True, (220, 220, 220))
        text_rect = text_surface.get_rect(center=surface_rect.center)
        self.controls_surface.blit(text_surface, text_rect)


    def handle_touch(self, pos):
        # Check which button was pressed
        if self.up_rect.collidepoint(pos):
            return "up"
        elif self.down_rect.collidepoint(pos):
            return "down"
        elif self.left_rect.collidepoint(pos):
            return "left"
        elif self.right_rect.collidepoint(pos):
            return "right"
        return None