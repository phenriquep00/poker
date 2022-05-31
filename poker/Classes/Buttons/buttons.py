import pygame


class Button:
    def __init__(self, surf, color, X, Y, rectW, rectH):
        self.surf = surf
        self.color = color
        self.X = X
        self.Y = Y
        self.rectW = rectW
        self.rectH = rectH
        self.handle_click = ''

    def draw(self):
        self.handle_click = pygame.draw.rect(
            surface=self.surf,
            color=self.color,
            rect=[
                (self.X, self.Y),
                (self.rectW, self.rectH)
            ],
            border_radius=5
        )
