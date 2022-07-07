from poker.functions import COLOR, FONT_M
import pygame as pg


class InputBox:

    def __init__(self, surf, x, y, w, h, text='Player'):
        self.surface = surf
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR.light_gray2
        self.text = text
        self.txt_surface = FONT_M.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR.green if self.active else COLOR.light_gray2
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT_M.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self):
        # Blit the text.
        self.surface.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(self.surface, self.color, self.rect, 2)

    def export_name(self):
        return self.text
