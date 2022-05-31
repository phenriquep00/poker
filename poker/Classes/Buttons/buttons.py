import pygame

from poker.Classes.Colors.colors import Colors

colors = Colors()


class Button:
    """
    Button class to normalize the style of every button in the project
    """
    def __init__(self, surf, color, X, Y, rectW, rectH, value):
        self.surf = surf
        self.color = color
        self.X = X
        self.Y = Y
        self.rectW = rectW
        self.rectH = rectH
        self.handle_click = ''
        self.value = value

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
