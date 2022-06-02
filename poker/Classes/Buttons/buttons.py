import pygame

from poker.functions import FONT_G, FONT_M, FONT_P, COLOR


class Button:
    """
    Button class to normalize the style of every button in the project
    """
    def __init__(self, surf, color, X, Y, rectW, rectH, value, font_size):
        """
        :param surf: pygame display object
        :param color: color of the button's background
        :param X: X coordinate for where the button will start (top-left)
        :param Y: Y coordinate for where the button will start (top-left)
        :param rectW: button width
        :param rectH: button height
        :param value: button text
        :param font_size: size of the font
        """
        self.surf = surf
        self.color = color
        self.X = X
        self.Y = Y
        self.rectW = rectW
        self.rectH = rectH
        self.handle_click = pygame.rect.Rect
        self.value = value
        self.font_size = font_size

    def draw(self):
        """
        set the handle_click attribute to become a pygame rect and make possible to handle rect events.
        Also add two other rectangles with smaller widths to create a border effect
        :return:
        None
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
            color=COLOR.light_gray2,
            rect=[
                (self.X, self.Y),
                (self.rectW, self.rectH)
            ],
            width=5,
            border_radius=5
        )
        pygame.draw.rect(
            surface=self.surf,
            color=COLOR.black,
            rect=[
                (self.X, self.Y),
                (self.rectW, self.rectH)
            ],
            width=3,
            border_radius=5
        )

        # add text to the button
        self.draw_font()

    def draw_font(self):
        """
        Get the information from the object initialization to acquire the font size then, renders the text and blit
        it inside the button
        :return:
        None
        """
        if 'G' in self.font_size.upper().strip():
            text = FONT_G.render(f'{self.value}', True, COLOR.white)
            self.surf.blit(text, ((self.X + 20), (self.Y + 25)))
        elif 'M' in self.font_size.upper().strip():
            text = FONT_M.render(f'{self.value}', True, COLOR.white)
            self.surf.blit(text, ((self.X + 15), (self.Y + 20)))
        elif 'P' in self.font_size.upper().strip():
            text = FONT_P.render(f'{self.value}', True, COLOR.white)
            self.surf.blit(text, ((self.X + 10), (self.Y + 15)))
