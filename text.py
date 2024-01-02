import pygame

class Text():
    def __init__(self, screen):
        self.TEXT_FONT = pygame.font.SysFont("Arial", 30)
        self.TITLE_FONT = pygame.font.SysFont("Arial", 120)
        self.UI_FONT = pygame.font.SysFont("Arial", 20)  
        self.screen = screen

    def draw_text(self, text, text_col, button):
        text_img =  self.TEXT_FONT.render(text, True, text_col)
        self.screen.blit(text_img, (button.center[0] - text_img.get_width()//2, button.center[1] - text_img.get_height()//2))

    def draw_text_title(self, text, text_col, button):
        text_img = self.TITLE_FONT.render(text, True, text_col)
        self.screen.blit(text_img, (button.center[0] - text_img.get_width()//2, button.center[1] - text_img.get_height()//2))

    def draw_UI_text(self, text, text_col, button):
        text_img = self.UI_FONT.render(text, True, text_col)
        self.screen.blit(text_img, (10, button.center[1] - text_img.get_height()//2))

    def draw_UI_text_centered(self, text, text_col, button):
        text_img = self.UI_FONT.render(text, True, text_col)
        self.screen.blit(text_img, (button.center[0] - text_img.get_width()//2, button.center[1] - text_img.get_height()//2))