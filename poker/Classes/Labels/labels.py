from poker.functions import blit_rotate_center, FONT_G, FONT_M, FONT_P
from poker.Classes.Colors.colors import Colors

colors = Colors()


class Label:
    def __init__(self, surf, X, Y, text, font, angle=0):
        self.surf = surf
        self.X = X
        self.Y = Y
        self.text = text
        self.font = font
        self.angle = angle

    def draw(self):
        """
            Get the information from the object initialization to acquire the font size then, renders the text and blit
            it inside the button
            :return:
            None
        """
        if 'G' in self.font.upper().strip():
            text = FONT_G.render(f'{self.text}', True, colors.white)
            blit_rotate_center(self.surf, text, (self.X, self.Y), self.angle)
        elif 'M' in self.font.upper().strip():
            text = FONT_M.render(f'{self.text}', True, colors.white)
            blit_rotate_center(self.surf, text, (self.X, self.Y), self.angle)
        elif 'P' in self.font.upper().strip():
            text = FONT_P.render(f'{self.text}', True, colors.white)
            blit_rotate_center(self.surf, text, (self.X, self.Y), self.angle)
