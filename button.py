
import pygame.font

from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from alien_invasion import AlienInvasion

class Button:
    """A class to build buttons for the game."""

    def __init__(self, game: 'AlienInvasion', msg):
       
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
                    self.settings.button_font_size)
        
        self.rect = pygame.Rect(0,0, self.settings.button_w,
                    self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Function to position the message"""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw(self):
        """Draws the message and the button on the screen
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    
    def check_clicked(self, mouse_pos):
        """Function to check if the mouse is clicking on the button"""
         
        return self.rect.collidepoint(mouse_pos)