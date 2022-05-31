import pygame

from poker.Classes.Colors.colors import Colors

colors = Colors()
pygame.init()
FONT_G = pygame.font.Font('freesansbold.ttf', 40)
FONT_M = pygame.font.Font('freesansbold.ttf', 24)
FONT_P = pygame.font.Font('freesansbold.ttf', 16)


class Button:
    """
    Button class to normalize the style of every button in the project
    """
    def __init__(self, surf, color, X, Y, rectW, rectH, value, font_size):
        self.surf = surf
        self.color = color
        self.X = X
        self.Y = Y
        self.rectW = rectW
        self.rectH = rectH
        self.handle_click = ''
        self.value = value
        self.font_size = font_size

    def draw(self):
        """
        set the handle_click attribute to become a pygame rect and make possible to handle rect events.
        Also create another rect, with width = 3 and a super light gray color, to add a border effect to all buttons
        """
        self.handle_click = pygame.draw.rect(
            surface=self.surf,
            color=self.color,
            rect=[
                (self.X, self.Y),
                (self.rectW, self.rectH)
            ],
            border_radius=5
        )

        # border rect
        pygame.draw.rect(
            surface=self.surf,
            color=colors.light_gray2,
            rect=[
                (self.X, self.Y),
                (self.rectW, self.rectH)
            ],
            width=3,
            border_radius=5
        )
        self.draw_font()

    def draw_font(self):
        if 'G' in self.font_size.upper().strip():
            text = FONT_G.render(f'{self.value}', True, colors.white)
            self.surf.blit(text, ((self.X + 20), (self.Y + 25)))
        elif 'M' in self.font_size.upper().strip():
            text = FONT_M.render(f'{self.value}', True, colors.white)
            self.surf.blit(text, ((self.X + 20), (self.Y + 40)))
        elif 'P' in self.font_size.upper().strip():
            text = FONT_P.render(f'{self.value}', True, colors.white)
            self.surf.blit(text, ((self.X + 20), (self.Y + 60)))
