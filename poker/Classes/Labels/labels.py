from poker.functions import blit_rotate_center, FONT_G, FONT_M, FONT_P, COLOR


class Label:
    def __init__(self, surf, X, Y, text, font, angle=0, color=COLOR.white):
        """

        :param surf: pygame display object to render the label
        :param X: X coordinate for the top-left position where the label will start
        :param Y: Y coordinate fot the top-left position where the label will start
        :param text: string with the to be rendered on the screen
        :param font: pygame Font object, accepts 'p' 'g' or 'm' as params
        :param angle: angle which the label will be displayed, accepts a number from 0 to 360
        """
        self.surf = surf
        self.X = X
        self.Y = Y
        self.text = text
        self.font = font
        self.angle = angle
        self.color = color

    def draw(self):
        """
            Get the information from the object initialization to acquire the font size then, renders the text and blit
            it inside the button
            :return:
            None
        """
        if 'G' in self.font.upper().strip():
            text = FONT_G.render(f'{self.text}', True, self.color)
            blit_rotate_center(self.surf, text, (self.X, self.Y), self.angle)
        elif 'M' in self.font.upper().strip():
            text = FONT_M.render(f'{self.text}', True, self.color)
            blit_rotate_center(self.surf, text, (self.X, self.Y), self.angle)
        elif 'P' in self.font.upper().strip():
            text = FONT_P.render(f'{self.text}', True, self.color)
            blit_rotate_center(self.surf, text, (self.X, self.Y), self.angle)

    def move(self, new_x, new_y):
        self.X = new_x
        self.Y = new_y
